from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    pincode = db.Column(db.String(10), nullable=True)
    nakshatra = db.Column(db.String(50), nullable=True)
    rasi = db.Column(db.String(50), nullable=True)
    gothra = db.Column(db.String(50), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    darshan_bookings = db.relationship('DarshanBooking', backref='user', lazy=True, cascade='all, delete-orphan')
    pooja_bookings = db.relationship('PoojaBooking', backref='user', lazy=True, cascade='all, delete-orphan')
    orders = db.relationship('Order', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.email}>'


class Temple(db.Model):
    __tablename__ = 'temples'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, index=True)
    deity = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    opening_time = db.Column(db.String(50), default="05:30 AM")
    closing_time = db.Column(db.String(50), default="09:00 PM")
    dress_code = db.Column(db.String(255), default="Traditional Dhoti/Veshti for Men, Saree or Salwar for Women")
    history = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    banner_url = db.Column(db.String(500), nullable=True)
    contact_phone = db.Column(db.String(50), nullable=True)
    contact_email = db.Column(db.String(100), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    darshan_slots = db.relationship('DarshanSlot', backref='temple', lazy=True, cascade='all, delete-orphan')
    poojas = db.relationship('Pooja', backref='temple', lazy=True, cascade='all, delete-orphan')
    prasadams = db.relationship('Prasadam', backref='temple', lazy=True, cascade='all, delete-orphan')
    darshan_bookings = db.relationship('DarshanBooking', backref='temple', lazy=True)
    pooja_bookings = db.relationship('PoojaBooking', backref='temple', lazy=True)
    reviews = db.relationship('Review', backref='temple', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Temple {self.name}>'


class DarshanSlot(db.Model):
    __tablename__ = 'darshan_slots'
    
    id = db.Column(db.Integer, primary_key=True)
    temple_id = db.Column(db.Integer, db.ForeignKey('temples.id'), nullable=False)
    slot_name = db.Column(db.String(100), nullable=False) # e.g. "Morning Suprabhata Slot"
    start_time = db.Column(db.String(20), nullable=False)  # "06:00 AM"
    end_time = db.Column(db.String(20), nullable=False)    # "08:30 AM"
    max_capacity = db.Column(db.Integer, default=150)
    price_general = db.Column(db.Float, default=0.0)      # Free Sarva Darshan
    price_special = db.Column(db.Float, default=100.0)    # Special Darshan ₹100
    price_vip = db.Column(db.Float, default=300.0)        # VIP / Sheegra Darshan ₹300
    is_active = db.Column(db.Boolean, default=True)

    def get_booked_count(self, darshan_date):
        """Returns total devotees booked for this slot on a given date"""
        total = db.session.query(db.func.sum(DarshanBooking.total_devotees)).filter(
            DarshanBooking.slot_id == self.id,
            DarshanBooking.darshan_date == darshan_date,
            DarshanBooking.status.in_(['Confirmed', 'Attended'])
        ).scalar()
        return total or 0

    def get_remaining_capacity(self, darshan_date):
        booked = self.get_booked_count(darshan_date)
        return max(0, self.max_capacity - booked)

    def __repr__(self):
        return f'<DarshanSlot {self.slot_name}>'


class DarshanBooking(db.Model):
    __tablename__ = 'darshan_bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    booking_reference = db.Column(db.String(50), unique=True, nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    temple_id = db.Column(db.Integer, db.ForeignKey('temples.id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('darshan_slots.id'), nullable=False)
    darshan_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'Free Sarva Darshan', 'Special Darshan', 'VIP Darshan'
    total_devotees = db.Column(db.Integer, default=1)
    ticket_price = db.Column(db.Float, default=0.0)
    total_amount = db.Column(db.Float, default=0.0)
    payment_status = db.Column(db.String(30), default='Completed') # 'Free', 'Completed', 'Refunded'
    payment_id = db.Column(db.String(100), nullable=True)
    qr_code_base64 = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(30), default='Confirmed') # 'Confirmed', 'Cancelled', 'Attended'
    cancellation_reason = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    devotees = db.relationship('Devotee', backref='darshan_booking', lazy=True, cascade='all, delete-orphan')
    slot = db.relationship('DarshanSlot', backref='bookings', lazy=True)


class Devotee(db.Model):
    __tablename__ = 'devotees'
    
    id = db.Column(db.Integer, primary_key=True)
    darshan_booking_id = db.Column(db.Integer, db.ForeignKey('darshan_bookings.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False) # Male, Female, Other
    id_type = db.Column(db.String(50), default='Aadhaar Card')
    id_number = db.Column(db.String(50), nullable=True)


class Pooja(db.Model):
    __tablename__ = 'poojas'
    
    id = db.Column(db.Integer, primary_key=True)
    temple_id = db.Column(db.Integer, db.ForeignKey('temples.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False) # "Sahasranama Archana", "Rudrabhishekam"
    deity = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration_mins = db.Column(db.Integer, default=30)
    items_included = db.Column(db.String(255), default="Flowers, Vibhuti, Kumkum, Prasadam Packet")
    is_active = db.Column(db.Boolean, default=True)
    image_url = db.Column(db.String(500), nullable=True)


class PoojaBooking(db.Model):
    __tablename__ = 'pooja_bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    booking_reference = db.Column(db.String(50), unique=True, nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    temple_id = db.Column(db.Integer, db.ForeignKey('temples.id'), nullable=False)
    pooja_id = db.Column(db.Integer, db.ForeignKey('poojas.id'), nullable=False)
    pooja_date = db.Column(db.Date, nullable=False)
    time_slot = db.Column(db.String(50), nullable=False) # "07:30 AM - 08:30 AM"
    devotee_name = db.Column(db.String(100), nullable=False)
    nakshatra = db.Column(db.String(50), nullable=True)
    rasi = db.Column(db.String(50), nullable=True)
    gothra = db.Column(db.String(50), nullable=True)
    sankalpam_wish = db.Column(db.Text, nullable=True)
    total_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(30), default='Completed')
    payment_id = db.Column(db.String(100), nullable=True)
    qr_code_base64 = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(30), default='Confirmed') # 'Confirmed', 'Completed', 'Cancelled'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    pooja = db.relationship('Pooja', backref='bookings', lazy=True)


class Product(db.Model):
    """Items sold in Online Pooja Store (Camphor, Diya, Garland, Pooja Kit etc.)"""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False) # Flowers & Garlands, Lamps & Diyas, Camphor & Dhoop, Kumkum & Turmeric, Pooja Kits
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, default=50)
    image_url = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, default=4.8)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Prasadam(db.Model):
    """Authentic Temple Prasadam (Laddu, Puliyodarai, Pongal, Panchamirtham)"""
    __tablename__ = 'prasadams'
    
    id = db.Column(db.Integer, primary_key=True)
    temple_id = db.Column(db.Integer, db.ForeignKey('temples.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    weight_grams = db.Column(db.Integer, default=250)
    expiry_days = db.Column(db.Integer, default=7)
    packaging_info = db.Column(db.String(200), default="Aroma-locked hygienic vacuum pouch")
    stock_quantity = db.Column(db.Integer, default=100)
    image_url = db.Column(db.String(500), nullable=True)
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Order(db.Model):
    """Store items and Prasadam unified orders"""
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    order_reference = db.Column(db.String(50), unique=True, nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    delivery_type = db.Column(db.String(50), default='Doorstep Delivery') # 'Doorstep Delivery' or 'Temple Counter Pickup'
    pickup_temple_id = db.Column(db.Integer, db.ForeignKey('temples.id'), nullable=True)
    
    shipping_name = db.Column(db.String(100), nullable=False)
    shipping_phone = db.Column(db.String(20), nullable=False)
    shipping_address = db.Column(db.String(255), nullable=True)
    shipping_city = db.Column(db.String(100), nullable=True)
    shipping_state = db.Column(db.String(100), nullable=True)
    shipping_pincode = db.Column(db.String(10), nullable=True)
    
    payment_status = db.Column(db.String(30), default='Completed')
    payment_id = db.Column(db.String(100), nullable=True)
    order_status = db.Column(db.String(50), default='Confirmed') # 'Confirmed', 'Preparing', 'Dispatched', 'Ready for Pickup', 'Delivered', 'Cancelled'
    tracking_number = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    pickup_temple = db.relationship('Temple', foreign_keys=[pickup_temple_id], lazy=True)


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    item_type = db.Column(db.String(20), nullable=False) # 'product' or 'prasadam'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    prasadam_id = db.Column(db.Integer, db.ForeignKey('prasadams.id'), nullable=True)
    item_name = db.Column(db.String(150), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)
    subtotal = db.Column(db.Float, nullable=False)
    
    # Relationships
    product = db.relationship('Product', lazy=True)
    prasadam = db.relationship('Prasadam', lazy=True)


class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    temple_id = db.Column(db.Integer, db.ForeignKey('temples.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, default=5)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
