from app import app, db
from models import Temple, DarshanSlot, Pooja, Product, Prasadam, User

with app.app_context():
    print(f"App name: {app.name}")
    temples_cnt = Temple.query.count()
    slots_cnt = DarshanSlot.query.count()
    poojas_cnt = Pooja.query.count()
    products_cnt = Product.query.count()
    prasadams_cnt = Prasadam.query.count()
    users_cnt = User.query.count()
    
    print("--- Database Verification ---")
    print(f"Total Temples: {temples_cnt}")
    print(f"Total Darshan Slots: {slots_cnt}")
    print(f"Total Pooja Sevas: {poojas_cnt}")
    print(f"Total Store Products: {products_cnt}")
    print(f"Total Prasadam Items: {prasadams_cnt}")
    print(f"Total Users: {users_cnt}")
    
    # Test client route requests
    client = app.test_client()
    routes = [
        '/',
        '/temples',
        '/temple/1',
        '/darshan/book/1',
        '/pooja/book/1',
        '/store',
        '/prasadam',
        '/cart',
        '/login',
        '/register'
    ]
    print("\n--- Route Health Checks ---")
    for r in routes:
        resp = client.get(r)
        print(f"GET {r:20} -> Status {resp.status_code}")
        assert resp.status_code == 200, f"Route {r} returned {resp.status_code}"
    
    print("\n[SUCCESS] All routes and templates verified successfully!")
