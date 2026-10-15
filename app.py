import os
from datetime import datetime, date, timedelta
from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, session, jsonify, abort
)
from config import Config
from models import (
    db, User, Temple, DarshanSlot, DarshanBooking, Devotee,
    Pooja, PoojaBooking, Product, Prasadam, Order, OrderItem, Review
)
from utils import generate_qr_code_base64, generate_reference_code, login_required, admin_required
from seed_data import seed_all_data

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Initialize database and sample seed data if tables are empty
with app.app_context():
    db.create_all()
    seed_all_data()

# Context processor for global template variables
@app.context_processor
def inject_global_data():
    current_user = None
    if 'user_id' in session:
        current_user = User.query.get(session['user_id'])
    
    # Calculate cart count from session
    cart = session.get('cart', {})
    cart_count = sum(item.get('quantity', 0) for item in cart.values())
    
    return {
        'current_user': current_user,
        'cart_count': cart_count,
        'app_name': Config.APP_NAME,
        'tagline': Config.TAGLINE,
        'currency': Config.CURRENCY,
        'demo_mode': Config.DEMO_MODE,
        'today': date.today()
    }


# ==============================================================================
# 1. HOME & PUBLIC DISCOVERY ROUTES
# ==============================================================================

@app.route('/')
def index():
    featured_temples = Temple.query.filter_by(is_featured=True, is_active=True).limit(6).all()
    if not featured_temples:
        featured_temples = Temple.query.filter_by(is_active=True).limit(6).all()
        
    popular_prasadams = Prasadam.query.filter_by(is_available=True).limit(4).all()
    special_poojas = Pooja.query.filter_by(is_active=True).limit(4).all()
    store_highlights = Product.query.filter_by(is_active=True).limit(4).all()
    
    # Unique deities and cities for search filters
    all_deities = [d[0] for d in db.session.query(Temple.deity).distinct().all() if d[0]]
    all_cities = [c[0] for c in db.session.query(Temple.city).distinct().all() if c[0]]

    # Sample Upcoming South Indian Festivals
    upcoming_festivals = [
        {"name": "Panguni Uthiram & Meenakshi Thirukalyanam", "date": "March 23, 2026", "temple": "Madurai & Mylapore", "desc": "Celebration of divine celestial weddings."},
        {"name": "Sri Rama Navami Brahmotsavam", "date": "March 27, 2026", "temple": "Rameswaram & Bhadrachalam", "desc": "Grand rathotsavam and special abhishekam."},
        {"name": "Chithirai Festival (Kallazhagar Vaigai Entry)", "date": "April 18, 2026", "temple": "Madurai", "desc": "Millions gather as Lord Kallazhagar enters River Vaigai."},
        {"name": "Vaikunta Ekadasi Special Darshan", "date": "December 20, 2026", "temple": "Srirangam & Tirupati", "desc": "Opening of Paramapada Vaasal (Gateway to Heaven)."}
    ]

    return render_template(
        'index.html',
        featured_temples=featured_temples,
        popular_prasadams=popular_prasadams,
        special_poojas=special_poojas,
        store_highlights=store_highlights,
        all_deities=all_deities,
        all_cities=all_cities,
        upcoming_festivals=upcoming_festivals
    )


@app.route('/temples')
def temples():
    search_query = request.args.get('q', '').strip()
    city_filter = request.args.get('city', '').strip()
    state_filter = request.args.get('state', '').strip()
    deity_filter = request.args.get('deity', '').strip()

    query = Temple.query.filter_by(is_active=True)

    if search_query:
        search = f"%{search_query}%"
        query = query.filter(
            (Temple.name.ilike(search)) |
            (Temple.deity.ilike(search)) |
            (Temple.city.ilike(search)) |
            (Temple.description.ilike(search))
        )
    if city_filter:
        query = query.filter(Temple.city.ilike(f"%{city_filter}%"))
    if state_filter:
        query = query.filter(Temple.state.ilike(f"%{state_filter}%"))
    if deity_filter:
        query = query.filter(Temple.deity.ilike(f"%{deity_filter}%"))

    temples_list = query.all()
    all_cities = [c[0] for c in db.session.query(Temple.city).distinct().all() if c[0]]
    all_states = [s[0] for s in db.session.query(Temple.state).distinct().all() if s[0]]

    return render_template(
        'temples.html',
        temples=temples_list,
        search_query=search_query,
        city_filter=city_filter,
        state_filter=state_filter,
        deity_filter=deity_filter,
        all_cities=all_cities,
        all_states=all_states
    )


@app.route('/temple/<int:temple_id>')
def temple_detail(temple_id):
    temple = Temple.query.get_or_404(temple_id)
    slots = DarshanSlot.query.filter_by(temple_id=temple.id, is_active=True).all()
    poojas = Pooja.query.filter_by(temple_id=temple.id, is_active=True).all()
    prasadams = Prasadam.query.filter_by(temple_id=temple.id, is_available=True).all()
    reviews = Review.query.filter_by(temple_id=temple.id).order_by(Review.created_at.desc()).all()

    return render_template(
        'temple_detail.html',
        temple=temple,
        slots=slots,
        poojas=poojas,
        prasadams=prasadams,
        reviews=reviews
    )


@app.route('/temple/<int:temple_id>/review', methods=['POST'])
@login_required
def add_temple_review(temple_id):
    temple = Temple.query.get_or_404(temple_id)
    rating = int(request.form.get('rating', 5))
    comment = request.form.get('comment', '').strip()
    
    if comment:
        user = User.query.get(session['user_id'])
        review = Review(
            temple_id=temple.id,
            user_name=user.name,
            rating=min(max(rating, 1), 5),
            comment=comment
        )
        db.session.add(review)
        db.session.commit()
        flash("Thank you! Your devotional experience review has been shared.", "success")
    return redirect(url_for('temple_detail', temple_id=temple_id))


# ==============================================================================
# 2. DARSHAN TICKET BOOKING & QR GENERATION
# ==============================================================================

@app.route('/darshan/book/<int:temple_id>', methods=['GET'])
def darshan_book(temple_id):
    temple = Temple.query.get_or_404(temple_id)
    slots = DarshanSlot.query.filter_by(temple_id=temple.id, is_active=True).all()
    
    # Pre-fill user data if logged in
    user_info = None
    if 'user_id' in session:
        user_info = User.query.get(session['user_id'])

    min_date = (date.today() + timedelta(days=0)).strftime('%Y-%m-%d')
    max_date = (date.today() + timedelta(days=90)).strftime('%Y-%m-%d')

    return render_template(
        'darshan_book.html',
        temple=temple,
        slots=slots,
        user_info=user_info,
        min_date=min_date,
        max_date=max_date
    )


@app.route('/api/darshan/availability', methods=['GET'])
def check_darshan_availability():
    slot_id = request.args.get('slot_id', type=int)
    date_str = request.args.get('date', type=str)
    
    if not slot_id or not date_str:
        return jsonify({'error': 'Missing slot_id or date'}), 400
        
    try:
        visit_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

    slot = DarshanSlot.query.get(slot_id)
    if not slot:
        return jsonify({'error': 'Slot not found'}), 404

    remaining = slot.get_remaining_capacity(visit_date)
    return jsonify({
        'slot_id': slot.id,
        'slot_name': slot.slot_name,
        'date': date_str,
        'max_capacity': slot.max_capacity,
        'remaining_capacity': remaining,
        'is_available': remaining > 0,
        'prices': {
            'Free Sarva Darshan': slot.price_general,
            'Special Darshan': slot.price_special,
            'VIP Sheegra Darshan': slot.price_vip
        }
    })


@app.route('/darshan/confirm', methods=['POST'])
@login_required
def darshan_confirm():
    temple_id = request.form.get('temple_id', type=int)
    slot_id = request.form.get('slot_id', type=int)
    darshan_date_str = request.form.get('darshan_date')
    category = request.form.get('category', 'Special Darshan')
    devotee_count = request.form.get('devotee_count', type=int, default=1)
    payment_method = request.form.get('payment_method', 'Mock UPI / Razorpay')

    temple = Temple.query.get_or_404(temple_id)
    slot = DarshanSlot.query.get_or_404(slot_id)

    try:
        darshan_date = datetime.strptime(darshan_date_str, '%Y-%m-%d').date()
    except Exception:
        flash("Invalid darshan date selected.", "danger")
        return redirect(url_for('darshan_book', temple_id=temple_id))

    if darshan_date < date.today():
        flash("Darshan date cannot be in the past.", "danger")
        return redirect(url_for('darshan_book', temple_id=temple_id))

    # Check slot remaining capacity
    remaining = slot.get_remaining_capacity(darshan_date)
    if remaining < devotee_count:
        flash(f"Sorry, only {remaining} slots remaining for this timing. Please select another slot or reduce devotees.", "danger")
        return redirect(url_for('darshan_book', temple_id=temple_id))

    # Calculate price per devotee
    ticket_price = 0.0
    if category == 'Special Darshan':
        ticket_price = slot.price_special
    elif category == 'VIP Sheegra Darshan':
        ticket_price = slot.price_vip
    else:
        ticket_price = slot.price_general

    total_amount = ticket_price * devotee_count

    # Generate unique booking reference
    booking_ref = generate_reference_code("DC-DAR")

    # Generate QR Code content
    qr_content = f"DIVINECONNECT DARSHAN TICKET\nRef: {booking_ref}\nTemple: {temple.name}\nDate: {darshan_date}\nSlot: {slot.start_time} - {slot.end_time}\nCategory: {category}\nDevotees: {devotee_count}"
    qr_base64 = generate_qr_code_base64(qr_content)

    # Create Darshan Booking
    booking = DarshanBooking(
        booking_reference=booking_ref,
        user_id=session['user_id'],
        temple_id=temple.id,
        slot_id=slot.id,
        darshan_date=darshan_date,
        category=category,
        total_devotees=devotee_count,
        ticket_price=ticket_price,
        total_amount=total_amount,
        payment_status='Free' if total_amount == 0 else 'Completed',
        payment_id=f"PAY_RZP_{generate_reference_code('')}" if total_amount > 0 else 'N/A',
        qr_code_base64=qr_base64,
        status='Confirmed'
    )
    db.session.add(booking)
    db.session.flush()

    # Add Devotee details
    primary_name = request.form.get('devotee_name_1', 'Devotee')
    for i in range(1, devotee_count + 1):
        name = request.form.get(f'devotee_name_{i}', f'Devotee {i}')
        age = request.form.get(f'devotee_age_{i}', type=int, default=30)
        gender = request.form.get(f'devotee_gender_{i}', 'Male')
        id_type = request.form.get(f'devotee_id_type_{i}', 'Aadhaar Card')
        id_number = request.form.get(f'devotee_id_num_{i}', 'XXXX-XXXX-XXXX')
        
        devotee = Devotee(
            darshan_booking_id=booking.id,
            name=name,
            age=age,
            gender=gender,
            id_type=id_type,
            id_number=id_number
        )
        db.session.add(devotee)

    db.session.commit()

    flash(f"Blessed Darshan ticket confirmed successfully! Booking Reference: {booking_ref}", "success")
    return redirect(url_for('ticket_view', booking_ref=booking_ref))


@app.route('/ticket/<string:booking_ref>')
def ticket_view(booking_ref):
    booking = DarshanBooking.query.filter_by(booking_reference=booking_ref).first_or_404()
    return render_template('ticket_view.html', booking=booking)


# ==============================================================================
# 3. POOJA BOOKING
# ==============================================================================

@app.route('/pooja/book/<int:temple_id>', methods=['GET'])
def pooja_book(temple_id):
    temple = Temple.query.get_or_404(temple_id)
    poojas = Pooja.query.filter_by(temple_id=temple.id, is_active=True).all()
    selected_pooja_id = request.args.get('pooja_id', type=int)
    
    user_info = None
    if 'user_id' in session:
        user_info = User.query.get(session['user_id'])

    # Standard Vedic Nakshatras and Rasis
    nakshatras = [
        "Aswini", "Bharani", "Krittika", "Rohini", "Mrigashiras", "Ardra",
        "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
        "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
        "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
        "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ]
    rasis = [
        "Mesham (Aries)", "Rishabham (Taurus)", "Mithunam (Gemini)", "Karkatakam (Cancer)",
        "Simham (Leo)", "Kanya (Virgo)", "Thulam (Libra)", "Vrischikam (Scorpio)",
        "Dhanusu (Sagittarius)", "Makaram (Capricorn)", "Kumbham (Aquarius)", "Meenam (Pisces)"
    ]

    min_date = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    max_date = (date.today() + timedelta(days=120)).strftime('%Y-%m-%d')

    return render_template(
        'pooja_book.html',
        temple=temple,
        poojas=poojas,
        selected_pooja_id=selected_pooja_id,
        user_info=user_info,
        nakshatras=nakshatras,
        rasis=rasis,
        min_date=min_date,
        max_date=max_date
    )


@app.route('/pooja/confirm', methods=['POST'])
@login_required
def pooja_confirm():
    temple_id = request.form.get('temple_id', type=int)
    pooja_id = request.form.get('pooja_id', type=int)
    pooja_date_str = request.form.get('pooja_date')
    time_slot = request.form.get('time_slot', 'Morning 07:30 AM - 08:30 AM')
    devotee_name = request.form.get('devotee_name', '').strip()
    nakshatra = request.form.get('nakshatra', '')
    rasi = request.form.get('rasi', '')
    gothra = request.form.get('gothra', '')
    sankalpam_wish = request.form.get('sankalpam_wish', '')

    temple = Temple.query.get_or_404(temple_id)
    pooja = Pooja.query.get_or_404(pooja_id)

    try:
        pooja_date = datetime.strptime(pooja_date_str, '%Y-%m-%d').date()
    except Exception:
        flash("Invalid pooja date selected.", "danger")
        return redirect(url_for('pooja_book', temple_id=temple_id))

    booking_ref = generate_reference_code("DC-PJA")

    qr_content = f"DIVINECONNECT POOJA PASS\nRef: {booking_ref}\nTemple: {temple.name}\nPooja: {pooja.name}\nDate: {pooja_date}\nDevotee: {devotee_name}\nNakshatra: {nakshatra}\nGothra: {gothra}"
    qr_base64 = generate_qr_code_base64(qr_content)

    pooja_booking = PoojaBooking(
        booking_reference=booking_ref,
        user_id=session['user_id'],
        temple_id=temple.id,
        pooja_id=pooja.id,
        pooja_date=pooja_date,
        time_slot=time_slot,
        devotee_name=devotee_name,
        nakshatra=nakshatra,
        rasi=rasi,
        gothra=gothra,
        sankalpam_wish=sankalpam_wish,
        total_amount=pooja.price,
        payment_status='Completed',
        payment_id=f"PAY_RZP_{generate_reference_code('')}",
        qr_code_base64=qr_base64,
        status='Confirmed'
    )
    db.session.add(pooja_booking)
    db.session.commit()

    flash(f"Divine Pooja registered successfully! Sankalpam Reference: {booking_ref}", "success")
    return redirect(url_for('pooja_ticket_view', booking_ref=booking_ref))


@app.route('/pooja-ticket/<string:booking_ref>')
def pooja_ticket_view(booking_ref):
    booking = PoojaBooking.query.filter_by(booking_reference=booking_ref).first_or_404()
    return render_template('pooja_ticket_view.html', booking=booking)


# ==============================================================================
# 4. ONLINE POOJA STORE & 5. PRASADAM ORDERING
# ==============================================================================

@app.route('/store')
def store():
    category = request.args.get('category', '').strip()
    search = request.args.get('q', '').strip()

    query = Product.query.filter_by(is_active=True)
    if category:
        query = query.filter_by(category=category)
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%") | Product.description.ilike(f"%{search}%"))

    products = query.all()
    categories = [
        "Flowers & Garlands", "Lamps & Diyas", "Camphor & Dhoop",
        "Kumkum & Turmeric", "Pooja Kits"
    ]
    return render_template('store.html', products=products, categories=categories, selected_category=category, search=search)


@app.route('/prasadam')
def prasadam():
    temple_id = request.args.get('temple_id', type=int)
    search = request.args.get('q', '').strip()

    query = Prasadam.query.filter_by(is_available=True)
    if temple_id:
        query = query.filter_by(temple_id=temple_id)
    if search:
        query = query.filter(Prasadam.name.ilike(f"%{search}%") | Prasadam.description.ilike(f"%{search}%"))

    prasadams = query.all()
    temples_list = Temple.query.filter_by(is_active=True).all()

    return render_template(
        'prasadam.html',
        prasadams=prasadams,
        temples=temples_list,
        selected_temple_id=temple_id,
        search=search
    )


# Cart Management APIs
@app.route('/api/cart/add', methods=['POST'])
def cart_add():
    data = request.get_json() or {}
    item_type = data.get('item_type') # 'product' or 'prasadam'
    item_id = str(data.get('item_id'))
    quantity = int(data.get('quantity', 1))

    if not item_type or not item_id:
        return jsonify({'success': False, 'message': 'Invalid item data'}), 400

    cart = session.get('cart', {})
    cart_key = f"{item_type}_{item_id}"

    # Fetch item metadata
    name, price, img, max_stock = "", 0.0, "", 10
    if item_type == 'product':
        p = Product.query.get(int(item_id))
        if not p: return jsonify({'success': False, 'message': 'Product not found'}), 404
        name, price, img, max_stock = p.name, p.price, p.image_url, p.stock_quantity
    elif item_type == 'prasadam':
        pr = Prasadam.query.get(int(item_id))
        if not pr: return jsonify({'success': False, 'message': 'Prasadam not found'}), 404
        name, price, img, max_stock = pr.name, pr.price, pr.image_url, pr.stock_quantity
    else:
        return jsonify({'success': False, 'message': 'Unknown item type'}), 400

    if cart_key in cart:
        new_qty = cart[cart_key]['quantity'] + quantity
        if new_qty > max_stock:
            return jsonify({'success': False, 'message': f'Only {max_stock} items available in stock'}), 400
        cart[cart_key]['quantity'] = new_qty
    else:
        cart[cart_key] = {
            'item_type': item_type,
            'item_id': int(item_id),
            'name': name,
            'price': price,
            'image_url': img,
            'quantity': quantity
        }

    session['cart'] = cart
    session.modified = True
    total_count = sum(item['quantity'] for item in cart.values())

    return jsonify({
        'success': True,
        'message': f"Added '{name}' to your sacred cart!",
        'cart_count': total_count
    })


@app.route('/api/cart/update', methods=['POST'])
def cart_update():
    data = request.get_json() or {}
    cart_key = data.get('cart_key')
    quantity = int(data.get('quantity', 1))

    cart = session.get('cart', {})
    if cart_key in cart:
        if quantity <= 0:
            del cart[cart_key]
        else:
            cart[cart_key]['quantity'] = quantity
        session['cart'] = cart
        session.modified = True

    total_count = sum(item['quantity'] for item in cart.values())
    subtotal = sum(item['price'] * item['quantity'] for item in cart.values())
    return jsonify({'success': True, 'cart_count': total_count, 'subtotal': subtotal})


@app.route('/api/cart/remove', methods=['POST'])
def cart_remove():
    data = request.get_json() or {}
    cart_key = data.get('cart_key')
    cart = session.get('cart', {})
    if cart_key in cart:
        del cart[cart_key]
        session['cart'] = cart
        session.modified = True
    total_count = sum(item['quantity'] for item in cart.values())
    subtotal = sum(item['price'] * item['quantity'] for item in cart.values())
    return jsonify({'success': True, 'cart_count': total_count, 'subtotal': subtotal})


@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    items = []
    subtotal = 0.0

    for key, val in cart.items():
        item_total = val['price'] * val['quantity']
        subtotal += item_total
        items.append({
            'key': key,
            'item_type': val['item_type'],
            'item_id': val['item_id'],
            'name': val['name'],
            'price': val['price'],
            'quantity': val['quantity'],
            'total': item_total,
            'image_url': val.get('image_url')
        })

    shipping_fee = 40.0 if items and subtotal < 500 else 0.0
    total_amount = subtotal + shipping_fee

    user_info = None
    if 'user_id' in session:
        user_info = User.query.get(session['user_id'])

    temples_list = Temple.query.filter_by(is_active=True).all()

    return render_template(
        'cart.html',
        items=items,
        subtotal=subtotal,
        shipping_fee=shipping_fee,
        total_amount=total_amount,
        user_info=user_info,
        temples=temples_list
    )


@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    cart = session.get('cart', {})
    if not cart:
        flash("Your devotional cart is empty.", "warning")
        return redirect(url_for('store'))

    delivery_type = request.form.get('delivery_type', 'Doorstep Delivery')
    pickup_temple_id = request.form.get('pickup_temple_id', type=int) if delivery_type == 'Temple Counter Pickup' else None

    shipping_name = request.form.get('shipping_name')
    shipping_phone = request.form.get('shipping_phone')
    shipping_address = request.form.get('shipping_address')
    shipping_city = request.form.get('shipping_city')
    shipping_state = request.form.get('shipping_state')
    shipping_pincode = request.form.get('shipping_pincode')

    # Calculate totals
    subtotal = sum(item['price'] * item['quantity'] for item in cart.values())
    shipping_fee = 40.0 if delivery_type == 'Doorstep Delivery' and subtotal < 500 else 0.0
    total_amount = subtotal + shipping_fee

    order_ref = generate_reference_code("DC-ORD")
    tracking_num = f"TRK-{generate_reference_code('')}"

    order = Order(
        order_reference=order_ref,
        user_id=session['user_id'],
        total_amount=total_amount,
        delivery_type=delivery_type,
        pickup_temple_id=pickup_temple_id,
        shipping_name=shipping_name,
        shipping_phone=shipping_phone,
        shipping_address=shipping_address if delivery_type == 'Doorstep Delivery' else 'Temple Counter Pickup',
        shipping_city=shipping_city if delivery_type == 'Doorstep Delivery' else 'Local Temple',
        shipping_state=shipping_state if delivery_type == 'Doorstep Delivery' else 'Tamil Nadu',
        shipping_pincode=shipping_pincode if delivery_type == 'Doorstep Delivery' else '600001',
        payment_status='Completed',
        payment_id=f"PAY_RZP_{generate_reference_code('')}",
        order_status='Confirmed',
        tracking_number=tracking_num
    )
    db.session.add(order)
    db.session.flush()

    # Add Order Items & reduce stock
    for key, val in cart.items():
        product_id = val['item_id'] if val['item_type'] == 'product' else None
        prasadam_id = val['item_id'] if val['item_type'] == 'prasadam' else None
        
        # Reduce inventory stock safely
        if product_id:
            prod = Product.query.get(product_id)
            if prod:
                prod.stock_quantity = max(0, prod.stock_quantity - val['quantity'])
        elif prasadam_id:
            prsd = Prasadam.query.get(prasadam_id)
            if prsd:
                prsd.stock_quantity = max(0, prsd.stock_quantity - val['quantity'])

        order_item = OrderItem(
            order_id=order.id,
            item_type=val['item_type'],
            product_id=product_id,
            prasadam_id=prasadam_id,
            item_name=val['name'],
            unit_price=val['price'],
            quantity=val['quantity'],
            subtotal=val['price'] * val['quantity']
        )
        db.session.add(order_item)

    db.session.commit()

    # Clear user's cart
    session['cart'] = {}
    session.modified = True

    flash(f"Order placed successfully! Devotional Reference: {order_ref}", "success")
    return redirect(url_for('checkout_success', order_ref=order_ref))


@app.route('/order/<string:order_ref>')
def checkout_success(order_ref):
    order = Order.query.filter_by(order_reference=order_ref).first_or_404()
    return render_template('checkout_success.html', order=order)


# ==============================================================================
# 6. USER AUTHENTICATION & DASHBOARD
# ==============================================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('user_dashboard'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        city = request.form.get('city', '').strip()
        state = request.form.get('state', '').strip()
        pincode = request.form.get('pincode', '').strip()
        nakshatra = request.form.get('nakshatra', '')
        rasi = request.form.get('rasi', '')
        gothra = request.form.get('gothra', '').strip()

        if not name or not email or not password:
            flash("Please enter your name, email, and password.", "danger")
            return redirect(url_for('register'))

        if password != confirm_password:
            flash("Passwords do not match. Please verify.", "danger")
            return redirect(url_for('register'))

        existing = User.query.filter_by(email=email).first()
        if existing:
            flash("An account already exists with this email address. Please sign in.", "warning")
            return redirect(url_for('login'))

        user = User(
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            nakshatra=nakshatra,
            rasi=rasi,
            gothra=gothra,
            is_admin=False
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        # Log in the user automatically
        session['user_id'] = user.id
        session['user_name'] = user.name
        session['is_admin'] = user.is_admin

        flash("Welcome to DivineConnect! Your devotee account has been created.", "success")
        return redirect(url_for('user_dashboard'))

    nakshatras = [
        "Aswini", "Bharani", "Krittika", "Rohini", "Mrigashiras", "Ardra",
        "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
        "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
        "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
        "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ]
    return render_template('auth/register.html', nakshatras=nakshatras)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('user_dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['is_admin'] = user.is_admin

            flash(f"Namaskaram, {user.name}! Successfully signed in.", "success")
            next_url = request.args.get('next')
            if user.is_admin and not next_url:
                return redirect(url_for('admin_dashboard'))
            return redirect(next_url or url_for('user_dashboard'))
        else:
            flash("Invalid email or password. Please try again.", "danger")

    return render_template('auth/login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been safely signed out. Om Shanti.", "info")
    return redirect(url_for('index'))


@app.route('/user/dashboard')
@login_required
def user_dashboard():
    user = User.query.get(session['user_id'])
    
    # User's Darshan bookings
    darshan_bookings = DarshanBooking.query.filter_by(user_id=user.id).order_by(DarshanBooking.darshan_date.desc()).all()
    
    # User's Pooja bookings
    pooja_bookings = PoojaBooking.query.filter_by(user_id=user.id).order_by(PoojaBooking.pooja_date.desc()).all()
    
    # User's Orders
    orders = Order.query.filter_by(user_id=user.id).order_by(Order.created_at.desc()).all()

    return render_template(
        'user/dashboard.html',
        user=user,
        darshan_bookings=darshan_bookings,
        pooja_bookings=pooja_bookings,
        orders=orders
    )


@app.route('/user/profile/update', methods=['POST'])
@login_required
def update_profile():
    user = User.query.get(session['user_id'])
    user.name = request.form.get('name', user.name).strip()
    user.phone = request.form.get('phone', user.phone).strip()
    user.address = request.form.get('address', user.address).strip()
    user.city = request.form.get('city', user.city).strip()
    user.state = request.form.get('state', user.state).strip()
    user.pincode = request.form.get('pincode', user.pincode).strip()
    user.nakshatra = request.form.get('nakshatra', user.nakshatra)
    user.rasi = request.form.get('rasi', user.rasi)
    user.gothra = request.form.get('gothra', user.gothra).strip()
    
    session['user_name'] = user.name
    db.session.commit()
    flash("Profile and devotee preferences updated successfully.", "success")
    return redirect(url_for('user_dashboard'))


@app.route('/booking/cancel/<string:booking_ref>', methods=['POST'])
@login_required
def cancel_booking(booking_ref):
    reason = request.form.get('cancellation_reason', 'Devotee requested cancellation')
    
    # Check darshan bookings
    darshan_b = DarshanBooking.query.filter_by(booking_reference=booking_ref, user_id=session['user_id']).first()
    if darshan_b:
        if darshan_b.darshan_date <= date.today():
            flash("Bookings for today or past dates cannot be cancelled as per temple regulations.", "warning")
            return redirect(url_for('user_dashboard'))
        darshan_b.status = 'Cancelled'
        darshan_b.cancellation_reason = reason
        darshan_b.payment_status = 'Refund Initiated' if darshan_b.total_amount > 0 else 'Free'
        db.session.commit()
        flash(f"Darshan ticket {booking_ref} cancelled. Refund will reflect in 3-5 working days.", "info")
        return redirect(url_for('user_dashboard'))

    # Check pooja bookings
    pooja_b = PoojaBooking.query.filter_by(booking_reference=booking_ref, user_id=session['user_id']).first()
    if pooja_b:
        if pooja_b.pooja_date <= date.today():
            flash("Pooja bookings for today cannot be cancelled.", "warning")
            return redirect(url_for('user_dashboard'))
        pooja_b.status = 'Cancelled'
        pooja_b.payment_status = 'Refund Initiated'
        db.session.commit()
        flash(f"Pooja booking {booking_ref} cancelled successfully.", "info")
        return redirect(url_for('user_dashboard'))

    flash("Booking not found.", "danger")
    return redirect(url_for('user_dashboard'))


# ==============================================================================
# 8. ADMIN DASHBOARD & MANAGEMENT
# ==============================================================================

@app.route('/admin')
@admin_required
def admin_dashboard():
    total_users = User.query.count()
    total_temples = Temple.query.count()
    total_darshan_bookings = DarshanBooking.query.count()
    total_pooja_bookings = PoojaBooking.query.count()
    total_orders = Order.query.count()

    # Revenue calculation
    darshan_revenue = db.session.query(db.func.sum(DarshanBooking.total_amount)).filter_by(status='Confirmed').scalar() or 0.0
    pooja_revenue = db.session.query(db.func.sum(PoojaBooking.total_amount)).filter_by(status='Confirmed').scalar() or 0.0
    order_revenue = db.session.query(db.func.sum(Order.total_amount)).filter(Order.order_status != 'Cancelled').scalar() or 0.0
    total_revenue = darshan_revenue + pooja_revenue + order_revenue

    recent_darshans = DarshanBooking.query.order_by(DarshanBooking.created_at.desc()).limit(5).all()
    recent_poojas = PoojaBooking.query.order_by(PoojaBooking.created_at.desc()).limit(5).all()
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()

    return render_template(
        'admin/dashboard.html',
        total_users=total_users,
        total_temples=total_temples,
        total_darshan_bookings=total_darshan_bookings,
        total_pooja_bookings=total_pooja_bookings,
        total_orders=total_orders,
        total_revenue=total_revenue,
        recent_darshans=recent_darshans,
        recent_poojas=recent_poojas,
        recent_orders=recent_orders
    )


@app.route('/admin/temples')
@admin_required
def admin_temples():
    temples_list = Temple.query.order_by(Temple.id.asc()).all()
    return render_template('admin/temples.html', temples=temples_list)


@app.route('/admin/temple/new', methods=['POST'])
@admin_required
def admin_temple_create():
    name = request.form.get('name')
    deity = request.form.get('deity')
    city = request.form.get('city')
    state = request.form.get('state')
    address = request.form.get('address')
    description = request.form.get('description')
    opening_time = request.form.get('opening_time', '05:30 AM')
    closing_time = request.form.get('closing_time', '09:00 PM')
    dress_code = request.form.get('dress_code', 'Traditional Hindu attire')
    image_url = request.form.get('image_url')
    is_featured = bool(request.form.get('is_featured'))

    temple = Temple(
        name=name, deity=deity, city=city, state=state, address=address,
        description=description, opening_time=opening_time, closing_time=closing_time,
        dress_code=dress_code, image_url=image_url, is_featured=is_featured, is_active=True
    )
    db.session.add(temple)
    db.session.commit()
    flash(f"Temple '{name}' added successfully.", "success")
    return redirect(url_for('admin_temples'))


@app.route('/admin/slots')
@admin_required
def admin_slots():
    temple_id = request.args.get('temple_id', type=int)
    temples_list = Temple.query.all()
    
    if temple_id:
        slots = DarshanSlot.query.filter_by(temple_id=temple_id).all()
        poojas = Pooja.query.filter_by(temple_id=temple_id).all()
    else:
        slots = DarshanSlot.query.all()
        poojas = Pooja.query.all()

    return render_template(
        'admin/slots.html',
        slots=slots,
        poojas=poojas,
        temples=temples_list,
        selected_temple_id=temple_id
    )


@app.route('/admin/slot/new', methods=['POST'])
@admin_required
def admin_slot_create():
    temple_id = request.form.get('temple_id', type=int)
    slot_name = request.form.get('slot_name')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    max_capacity = request.form.get('max_capacity', type=int, default=150)
    price_special = request.form.get('price_special', type=float, default=100.0)
    price_vip = request.form.get('price_vip', type=float, default=300.0)

    slot = DarshanSlot(
        temple_id=temple_id,
        slot_name=slot_name,
        start_time=start_time,
        end_time=end_time,
        max_capacity=max_capacity,
        price_general=0.0,
        price_special=price_special,
        price_vip=price_vip,
        is_active=True
    )
    db.session.add(slot)
    db.session.commit()
    flash(f"Darshan Slot '{slot_name}' added successfully.", "success")
    return redirect(url_for('admin_slots', temple_id=temple_id))


@app.route('/admin/pooja/new', methods=['POST'])
@admin_required
def admin_pooja_create():
    temple_id = request.form.get('temple_id', type=int)
    name = request.form.get('name')
    deity = request.form.get('deity')
    description = request.form.get('description')
    price = request.form.get('price', type=float, default=101.0)
    duration_mins = request.form.get('duration_mins', type=int, default=30)
    items_included = request.form.get('items_included', 'Vibhuti, Kumkum, Prasadam Packet')

    pooja = Pooja(
        temple_id=temple_id,
        name=name,
        deity=deity,
        description=description,
        price=price,
        duration_mins=duration_mins,
        items_included=items_included,
        is_active=True
    )
    db.session.add(pooja)
    db.session.commit()
    flash(f"Pooja seva '{name}' added successfully.", "success")
    return redirect(url_for('admin_slots', temple_id=temple_id))


@app.route('/admin/store')
@admin_required
def admin_store():
    products = Product.query.all()
    prasadams = Prasadam.query.all()
    temples_list = Temple.query.all()
    return render_template('admin/store.html', products=products, prasadams=prasadams, temples=temples_list)


@app.route('/admin/product/new', methods=['POST'])
@admin_required
def admin_product_create():
    name = request.form.get('name')
    category = request.form.get('category')
    description = request.form.get('description')
    price = request.form.get('price', type=float)
    stock = request.form.get('stock_quantity', type=int, default=50)
    image_url = request.form.get('image_url')

    prod = Product(
        name=name, category=category, description=description,
        price=price, stock_quantity=stock, image_url=image_url, is_active=True
    )
    db.session.add(prod)
    db.session.commit()
    flash(f"Product '{name}' added to store inventory.", "success")
    return redirect(url_for('admin_store'))


@app.route('/admin/prasadam/new', methods=['POST'])
@admin_required
def admin_prasadam_create():
    temple_id = request.form.get('temple_id', type=int)
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price', type=float)
    weight_grams = request.form.get('weight_grams', type=int, default=250)
    expiry_days = request.form.get('expiry_days', type=int, default=7)
    packaging_info = request.form.get('packaging_info', 'Hygienic sealed box')
    stock = request.form.get('stock_quantity', type=int, default=100)
    image_url = request.form.get('image_url')

    prasadam = Prasadam(
        temple_id=temple_id, name=name, description=description, price=price,
        weight_grams=weight_grams, expiry_days=expiry_days, packaging_info=packaging_info,
        stock_quantity=stock, image_url=image_url, is_available=True
    )
    db.session.add(prasadam)
    db.session.commit()
    flash(f"Prasadam '{name}' added successfully.", "success")
    return redirect(url_for('admin_store'))


@app.route('/admin/orders')
@admin_required
def admin_orders():
    darshan_bookings = DarshanBooking.query.order_by(DarshanBooking.darshan_date.desc()).all()
    pooja_bookings = PoojaBooking.query.order_by(PoojaBooking.pooja_date.desc()).all()
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template(
        'admin/orders.html',
        darshan_bookings=darshan_bookings,
        pooja_bookings=pooja_bookings,
        orders=orders
    )


@app.route('/admin/order/status', methods=['POST'])
@admin_required
def admin_update_order_status():
    order_id = request.form.get('order_id', type=int)
    status = request.form.get('order_status')
    order = Order.query.get_or_404(order_id)
    order.order_status = status
    db.session.commit()
    flash(f"Order #{order.order_reference} status updated to {status}.", "success")
    return redirect(url_for('admin_orders'))


@app.route('/admin/darshan/status', methods=['POST'])
@admin_required
def admin_update_darshan_status():
    booking_id = request.form.get('booking_id', type=int)
    status = request.form.get('status')
    booking = DarshanBooking.query.get_or_404(booking_id)
    booking.status = status
    db.session.commit()
    flash(f"Darshan booking #{booking.booking_reference} status updated to {status}.", "success")
    return redirect(url_for('admin_orders'))


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n=======================================================")
    print("DivineConnect Web Application Starting...")
    print(f"Devotee URL  : http://localhost:{port}")
    print(f"Admin Portal : http://localhost:{port}/admin")
    print("Default Admin: admin@divineconnect.com / admin123")
    print("Devotee User : devotee@divineconnect.com / devotee123")
    print("=======================================================\n")
    app.run(host='0.0.0.0', port=port, debug=False)
