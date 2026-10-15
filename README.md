# 🛕 DivineConnect – Smart Temple Booking & Devotional Services

> **Traditional South Indian Devotional Pilgrimage Management Web Platform**  
> Built with **Python Flask**, **MySQL / SQLite**, **HTML5/Bootstrap 5**, **QR Code e-Pass Generation**, and **Razorpay Test Payment Integration**.

---

## 🌟 Overview & Key Highlights

**DivineConnect** is a responsive web application designed with an authentic South Indian temple aesthetic (deep sacred maroon, vibrant chandan saffron, golden kumbam accents, and warm temple cream).

It addresses all key devotional needs for pilgrims and temples:
1. **Majestic Home Page**: Temple discovery with search by deity, city, state, or name; upcoming festival calendars (Panguni Uthiram, Chithirai Thiruvizha, Brahmotsavam); quick navigation tiles.
2. **Temple Profiles & Darshan Pass Reservations**:
   - Detailed temple kshetram history, pradhana deities, timings, and strict traditional dress codes.
   - Slot reservation with real-time remaining capacity check to prevent double booking.
   - Categories: **Free Sarva Darshan**, **Special Darshan (₹100)**, and **VIP Sheegra Darshan (₹300)**.
   - Individual devotee details capture (Name, Age, Gender, Govt ID Proof type & number).
   - Generates unique reference code (`DC-DAR-XXXXXX`) and instant scannable **QR-Code e-Ticket** with printable pass format.
3. **Sacred Vedic Pooja Bookings**:
   - Recitation sevas: *Sahasranama Archana*, *Maha Rudrabhishekam*, *Kalyanotsavam*, *Navapashanam Abhishekam*.
   - Devotee's Vedic Sankalpam: 27 Vedic Nakshatras, 12 Rasis, Gothram, and customized prayer prarthana.
   - Generates digital Pooja Sankalpam Token with priest verification QR code.
4. **Online Pooja Items Store**:
   - Fresh Madurai Malli (Jasmine) garlands, brass panchamukhi deepams, pure Bhimseni camphor, organic Mysore chandan paste, and all-in-one daily pooja kits.
   - Category filtering, real-time stock counters, add-to-cart, and quantity management.
5. **Authentic Consecrated Temple Prasadam**:
   - Real GI-tagged and consecrated temple offerings: Tirumala Ghee Laddu, Palani Panchamirtham, Madurai Puliyodarai, Thanjavur Sakkarai Pongal, Srirangam Kancheepuram Idli.
   - Complete transparency on ingredients, packaging details, and shelf-life expiration.
   - Choice of **Doorstep Express Devotional Delivery** or **Temple Counter Pickup**.
6. **Unified Devotee Dashboard & Auth**:
   - User registration and login with 1-click test credentials fill.
   - Saved family devotee details, view upcoming/past darshan tokens, pooja passes, and order tracking.
   - Cancellation rules and refund status tracker.
7. **Razorpay Test Payment Gateway**:
   - Test sandbox modal supporting UPI (GPay, PhonePe, Paytm), Debit/Credit Cards, and Net Banking with instant backend verification.
8. **Admin Control Portal**:
   - Central Devaswom management: Add temples, configure slot capacities, add pooja sevas, monitor revenue, track attendance, and update order dispatch stages.

---

## 🗂️ Project Directory Structure

```
DivineConnect/
├── app.py                      # Core Flask Application & API Routes
├── config.py                   # Configuration (MySQL with SQLite automatic fallback)
├── models.py                   # SQLAlchemy Models (12 interconnected tables)
├── seed_data.py                # Populates realistic South Indian temple demo data
├── utils.py                    # QR Code Base64 generator, reference generators, auth decorators
├── test_app.py                 # Automated route health test suite
├── test_flows.py               # End-to-end integration test suite
├── requirements.txt            # Python dependencies
├── run.bat                     # 1-Click launcher script for Windows
├── README.md                   # Complete documentation
│
├── database/
│   ├── schema.sql              # Pure MySQL DDL schema
│   └── seeds.sql               # Pure MySQL INSERT seed data
│
├── static/
│   ├── css/
│   │   └── style.css           # Custom South Indian devotional theme & print stylesheet
│   └── js/
│       ├── main.js             # Cart management, dynamic slot quota checker, devotee form
│       └── payment.js          # Razorpay test payment modal simulation
│
└── templates/
    ├── base.html               # Master layout with responsive navbar, badges & footer
    ├── index.html              # Home page with hero, search, upcoming festivals & prasad
    ├── temples.html            # Temple directory with multi-criteria filters
    ├── temple_detail.html      # Individual temple page with darshan, poojas, reviews
    ├── darshan_book.html       # Darshan ticket reservation & devotee forms
    ├── pooja_book.html         # Pooja booking & Vedic sankalpam form
    ├── ticket_view.html        # Printable Darshan E-Ticket with QR Code
    ├── pooja_ticket_view.html  # Printable Pooja Sankalpam Pass with QR Code
    ├── store.html              # Online Pooja Items Store catalog
    ├── prasadam.html           # Temple Prasadam ordering catalog
    ├── cart.html               # Sacred Cart, delivery/pickup selection & checkout
    ├── checkout_success.html   # Order confirmation & receipt with tracking timeline
    │
    ├── auth/
    │   ├── login.html          # Sign-in with 1-click demo login buttons
    │   └── register.html       # Devotee registration with Vedic preferences
    │
    ├── user/
    │   └── dashboard.html      # Devotee dashboard (tickets, poojas, orders, cancellation)
    │
    └── admin/
        ├── dashboard.html      # Admin overview metrics, revenue & quick actions
        ├── temples.html        # Manage temples (Add/edit/view)
        ├── slots.html          # Manage darshan quota slots & pooja schedules
        ├── store.html          # Manage products, prasadams & stock inventory
        └── orders.html         # Manage gate verification & order fulfillment
```

---

## ⚙️ Quick Start & Step-by-Step Installation

### Step 1: Open the Project Directory
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\DivineConnect
```

### Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
You can start the server using either:

**Option A (1-Click on Windows):**
Double-click `run.bat`

**Option B (Command Line):**
```bash
python app.py
```

Open your browser and navigate to:  
👉 **http://localhost:5000**

---

## 🔑 Pre-Configured Demo Accounts

For testing, use these 1-click credentials available on the login page:

| Role | Email | Password | Access |
|---|---|---|---|
| **Devotee** | `devotee@divineconnect.com` | `devotee123` | Book darshan, pooja, view QR passes, order items |
| **Admin** | `admin@divineconnect.com` | `admin123` | Access `/admin`, manage temples, slots, stock & orders |

---

## 🗄️ Database Configuration (MySQL & SQLite)

### Automatic SQLite Zero-Config Fallback (Out of the Box)
If MySQL is not installed or running locally, DivineConnect automatically falls back to an embedded SQLite database (`divineconnect.db`) and seeds all 8 South Indian temples, 40 darshan slots, 12 poojas, 8 store products, and 7 prasadams automatically. **You don't need any manual setup to run the app right now!**

### Connecting to MySQL (Optional / Production)
To connect your local or cloud MySQL server:
1. Create database:
   ```sql
   CREATE DATABASE divineconnect CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
2. Import schema and seed data:
   ```bash
   mysql -u root -p divineconnect < database/schema.sql
   mysql -u root -p divineconnect < database/seeds.sql
   ```
3. Set your environment variables in PowerShell or `.env`:
   ```powershell
   $env:MYSQL_USER = "root"
   $env:MYSQL_PASSWORD = "your_mysql_password"
   $env:MYSQL_HOST = "localhost"
   $env:MYSQL_PORT = "3306"
   $env:MYSQL_DB = "divineconnect"
   ```
   Or set `DATABASE_URL`:
   ```powershell
   $env:DATABASE_URL = "mysql+pymysql://root:your_mysql_password@localhost:3306/divineconnect"
   ```

---

## 🧪 Automated Test Verification

Run the automated test suite anytime to verify all 10 public routes and 5 end-to-end user journeys:
```powershell
# Route and model test
python test_app.py

# End-to-end integration flow test (Darshan booking + QR, Pooja + Sankalpam, Cart Checkout, Admin)
python test_flows.py
```

---

## 📜 Disclaimer
*DivineConnect is an educational prototype and demonstration platform. All temple schedules, ticket prices, and booking availability are demonstration data simulated for pilgrimage management.*
