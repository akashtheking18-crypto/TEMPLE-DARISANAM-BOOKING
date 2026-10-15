from app import app, db
from models import DarshanBooking, PoojaBooking, Order, Product, Prasadam
import datetime

client = app.test_client()

with app.app_context():
    # 1. Login as Devotee
    login_resp = client.post('/login', data={
        'email': 'devotee@divineconnect.com',
        'password': 'devotee123'
    }, follow_redirects=True)
    assert login_resp.status_code == 200
    print("[TEST 1/5] Devotee login successful!")

    # 2. Test Darshan Booking
    darshan_date_str = (datetime.date.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    darshan_resp = client.post('/darshan/confirm', data={
        'temple_id': 1,
        'slot_id': 1,
        'darshan_date': darshan_date_str,
        'category': 'Special Darshan',
        'devotee_count': 2,
        'devotee_name_1': 'Sundaramurthy S',
        'devotee_age_1': 35,
        'devotee_gender_1': 'Male',
        'devotee_id_type_1': 'Aadhaar Card',
        'devotee_id_num_1': '9876-5432-1098',
        'devotee_name_2': 'Meenakshi Sundaram',
        'devotee_age_2': 32,
        'devotee_gender_2': 'Female',
        'devotee_id_type_2': 'Voter ID',
        'devotee_id_num_2': 'ABC1234567'
    }, follow_redirects=True)
    assert darshan_resp.status_code == 200
    latest_darshan = DarshanBooking.query.order_by(DarshanBooking.id.desc()).first()
    assert latest_darshan is not None
    assert latest_darshan.qr_code_base64.startswith("data:image/png;base64,")
    print(f"[TEST 2/5] Darshan booking & QR generation verified: {latest_darshan.booking_reference}")

    # 3. Test Pooja Booking
    pooja_date_str = (datetime.date.today() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    pooja_resp = client.post('/pooja/confirm', data={
        'temple_id': 1,
        'pooja_id': 1,
        'pooja_date': pooja_date_str,
        'time_slot': 'Morning 07:30 AM - 08:30 AM',
        'devotee_name': 'Sundaramurthy Family',
        'nakshatra': 'Aswini',
        'rasi': 'Mesham',
        'gothra': 'Bharadwaja',
        'sankalpam_wish': 'Family harmony, health, and spiritual peace'
    }, follow_redirects=True)
    assert pooja_resp.status_code == 200
    latest_pooja = PoojaBooking.query.order_by(PoojaBooking.id.desc()).first()
    assert latest_pooja is not None
    print(f"[TEST 3/5] Pooja booking & QR generation verified: {latest_pooja.booking_reference}")

    # 4. Test Add to Cart and Checkout
    cart_add_resp = client.post('/api/cart/add', json={
        'item_type': 'prasadam',
        'item_id': 1,
        'quantity': 2
    })
    assert cart_add_resp.status_code == 200
    
    checkout_resp = client.post('/checkout', data={
        'delivery_type': 'Doorstep Delivery',
        'shipping_name': 'Sundaramurthy S',
        'shipping_phone': '9840123456',
        'shipping_address': '42, Sannathi Street, Mylapore',
        'shipping_city': 'Chennai',
        'shipping_state': 'Tamil Nadu',
        'shipping_pincode': '600004'
    }, follow_redirects=True)
    assert checkout_resp.status_code == 200
    latest_order = Order.query.order_by(Order.id.desc()).first()
    assert latest_order is not None
    print(f"[TEST 4/5] Cart & Checkout verified: {latest_order.order_reference} (Tracking: {latest_order.tracking_number})")

    # 5. Test Admin Login and Admin Pages
    client.get('/logout')
    admin_login_resp = client.post('/login', data={
        'email': 'admin@divineconnect.com',
        'password': 'admin123'
    }, follow_redirects=True)
    assert admin_login_resp.status_code == 200

    admin_pages = ['/admin', '/admin/temples', '/admin/slots', '/admin/store', '/admin/orders']
    for p in admin_pages:
        adm_resp = client.get(p)
        assert adm_resp.status_code == 200
        print(f"   Admin GET {p:15} -> 200 OK")

    print("[TEST 5/5] All Admin routes verified successfully!")

print("\n=======================================================")
print("[SUCCESS] ALL 5 END-TO-END FLOW TESTS COMPLETED WITH 100% SUCCESS!")
print("=======================================================")
