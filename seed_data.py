"""
DivineConnect - Sample Data Seeder
Populates rich demonstration temples, darshan slots, poojas, products, and prasadams.
All sample data is clearly marked as demonstration / simulation data.
"""

from models import db, User, Temple, DarshanSlot, Pooja, Product, Prasadam, Review
from werkzeug.security import generate_password_hash

def seed_all_data():
    # 1. Create Default Users (Admin and Sample Devotee)
    admin = User.query.filter_by(email='admin@divineconnect.com').first()
    if not admin:
        admin = User(
            name="DivineConnect Temple Admin",
            email="admin@divineconnect.com",
            password_hash=generate_password_hash("admin123"),
            phone="9876543210",
            address="Devaswom Board Office, Anna Salai",
            city="Chennai",
            state="Tamil Nadu",
            pincode="600002",
            nakshatra="Rohini",
            rasi="Vrishabha",
            gothra="Kashyapa",
            is_admin=True
        )
        db.session.add(admin)

    devotee = User.query.filter_by(email='devotee@divineconnect.com').first()
    if not devotee:
        devotee = User(
            name="Sundaramurthy Swaminathan",
            email="devotee@divineconnect.com",
            password_hash=generate_password_hash("devotee123"),
            phone="9840123456",
            address="42, Sannathi Street, Mylapore",
            city="Chennai",
            state="Tamil Nadu",
            pincode="600004",
            nakshatra="Aswini",
            rasi="Mesham",
            gothra="Bharadwaja",
            is_admin=False
        )
        db.session.add(devotee)

    db.session.commit()

    # 2. Sample South Indian Temples (Demonstration Data)
    if Temple.query.count() == 0:
        temples_data = [
            {
                "name": "Arulmigu Meenakshi Sundareswarar Temple",
                "deity": "Goddess Meenakshi & Lord Sundareswarar (Shiva)",
                "city": "Madurai",
                "state": "Tamil Nadu",
                "address": "Madurai Main, Madurai, Tamil Nadu 625001",
                "description": "One of the greatest architectural masterpieces of South India, featuring 14 soaring gopurams encrusted with thousands of mythological figures. Revered for divine grace, arts, and cultural heritage.",
                "opening_time": "05:00 AM",
                "closing_time": "09:30 PM",
                "dress_code": "Strict traditional attire: Veshti/Dhoti or Pyjama with Kurta for Men; Saree, Half-Saree or Chudidhar with Dupatta for Women. Jeans and western wear prohibited.",
                "history": "Built during the Pandyan era and lavishly expanded by Thirumalai Nayak in the 16th-17th centuries, the temple represents cosmic equilibrium between Shakti and Shiva.",
                "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 452 234 4360",
                "contact_email": "darshan@maduraimeenakshi.gov.demo",
                "is_featured": True
            },
            {
                "name": "Sri Venkateswara Swamy Temple",
                "deity": "Lord Venkateswara / Balaji (Maha Vishnu)",
                "city": "Tirupati",
                "state": "Andhra Pradesh",
                "address": "S Mada St, Tirumala, Tirupati, Andhra Pradesh 517504",
                "description": "Perched atop the sacred Seven Hills of Seshachalam, this is the Kaliyuga Vaikuntam and one of the most visited pilgrimage destinations on earth, where Lord Srinivasa grants boons.",
                "opening_time": "03:00 AM",
                "closing_time": "11:30 PM",
                "dress_code": "Traditional White Dhoti/Pancha with Uttariyam for Men; Traditional Saree or Salwar Kameez with Dupatta for Women.",
                "history": "Ancient temple mentioned in early Sangam literature and celebrated by the Alvars. Supported over dynasties by Pallavas, Cholas, Pandyas, and Krishnadevaraya of Vijayanagara.",
                "image_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 877 227 7777",
                "contact_email": "helpdesk@ttdseva.gov.demo",
                "is_featured": True
            },
            {
                "name": "Brihadeeswarar Temple (Thanjai Periya Kovil)",
                "deity": "Lord Shiva (Peruvudaiyar / Brihadisvara)",
                "city": "Thanjavur",
                "state": "Tamil Nadu",
                "address": "Membalam Rd, Balaganapathy Nagar, Thanjavur, Tamil Nadu 613007",
                "description": "UNESCO World Heritage Site and pinnacle of Chola imperial granite architecture. Features a 216-foot vimana crowned by an 80-tonne single granite Kumbam stone.",
                "opening_time": "06:00 AM",
                "closing_time": "08:30 PM",
                "dress_code": "Decent traditional attire recommended. Footwear strictly prohibited beyond the outer Raja Gopuram threshold.",
                "history": "Consecrated in 1010 CE by the legendary Chola Emperor Raja Raja Chola I. An engineering marvel constructed entirely of solid granite without binding mortar.",
                "image_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 4362 274 476",
                "contact_email": "periyakovil@thanjavurchola.gov.demo",
                "is_featured": True
            },
            {
                "name": "Arulmigu Ramanathaswamy Temple",
                "deity": "Lord Ramanathaswamy (Shiva - Jyotirlinga)",
                "city": "Rameswaram",
                "state": "Tamil Nadu",
                "address": "Rameswaram Island, Ramanathapuram, Tamil Nadu 623526",
                "description": "Famed for having the longest sculptured pillared corridor among Hindu temples and 22 sacred teerthams (holy wells) where pilgrims take ritual purificatory baths.",
                "opening_time": "05:00 AM",
                "closing_time": "09:00 PM",
                "dress_code": "Devotees taking bath in Teerthams must change into dry traditional attire before entering inner darshan sanctum.",
                "history": "Established according to Ramayana tradition where Lord Sri Rama consecrated the Shiva Linga made by Sita Devi before crossing to Lanka.",
                "image_url": "https://images.unsplash.com/photo-1544717302-de2939b7ef71?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1544717302-de2939b7ef71?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 4573 221 223",
                "contact_email": "seva@rameswaramramesh.gov.demo",
                "is_featured": True
            },
            {
                "name": "Arulmigu Dhandayuthapani Swamy Temple",
                "deity": "Lord Murugan (Bala Dhandayuthapani)",
                "city": "Palani",
                "state": "Tamil Nadu",
                "address": "Giri Veedhi, Palani, Dindigul District, Tamil Nadu 624601",
                "description": "One of the Six Holy Abodes (Arupadai Veedu) of Lord Murugan. The deity idol was consecrated by the revered Siddha Bogar using Navapashanam (nine medicinal substances).",
                "opening_time": "05:30 AM",
                "closing_time": "09:30 PM",
                "dress_code": "Traditional South Indian costume. Hairstyle / Head shave (Mottai) tokens available separately.",
                "history": "Celebrated abode where Lord Murugan stood as an ascetic youth renouncing worldly attachments for the celestial fruit of divine knowledge (Gnana Pazham).",
                "image_url": "https://images.unsplash.com/photo-1621644820613-333d1c442345?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1621644820613-333d1c442345?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 4545 242 236",
                "contact_email": "dhandayuthapani@palani.gov.demo",
                "is_featured": True
            },
            {
                "name": "Guruvayur Sri Krishna Temple",
                "deity": "Lord Krishna (Guruvayurappan / Unnikrishnan)",
                "city": "Guruvayur",
                "state": "Kerala",
                "address": "Guruvayur Devaswom, Thrissur, Kerala 680101",
                "description": "Revered as the 'Bhuloka Vaikuntam'. The four-armed idol of Lord Vishnu/Krishna holds the conch, discus, mace, and lotus, and is bathed daily in holy water, milk, and rosewater.",
                "opening_time": "03:00 AM",
                "closing_time": "09:30 PM",
                "dress_code": "Strict traditional Kerala costume: Mundu (Veshti) without shirt/banian for men; Saree or traditional Pavada for women. Electronic gadgets strictly prohibited.",
                "history": "Consecrated according to folklore by Guru (Jupiter) and Vayu (Wind God) after the submergence of Dwaraka at the dawn of Kaliyuga.",
                "image_url": "https://images.unsplash.com/photo-1609137144822-421714856f67?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1609137144822-421714856f67?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 487 255 6335",
                "contact_email": "devaswom@guruvayurappan.gov.demo",
                "is_featured": False
            },
            {
                "name": "Kapaleeshwarar Temple",
                "deity": "Lord Shiva (Kapaleeshwarar) & Karpagambal",
                "city": "Chennai",
                "state": "Tamil Nadu",
                "address": "Vada Agrahara, Mylapore, Chennai, Tamil Nadu 600004",
                "description": "Ancient Dravidian temple in the cultural heart of Mylapore, Chennai. Featuring a 120-foot rainbow gopuram, sacred temple tank, and vibrant Panguni Peruvizha car festival.",
                "opening_time": "06:00 AM",
                "closing_time": "09:00 PM",
                "dress_code": "Traditional Hindu devotional clothing.",
                "history": "Immortalized in the 7th century Tevaram hymns of Nayanmars. Goddess Parvati worshipped here in the divine form of a peacock (Mayil), giving Mylapore its name.",
                "image_url": "https://images.unsplash.com/photo-1616428255955-46eb61fa40a3?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1616428255955-46eb61fa40a3?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 44 2464 1670",
                "contact_email": "mylapore@kapaleeshwarar.gov.demo",
                "is_featured": False
            },
            {
                "name": "Sri Ranganathaswamy Temple",
                "deity": "Lord Ranganatha (Reclining Maha Vishnu)",
                "city": "Srirangam",
                "state": "Tamil Nadu",
                "address": "Srirangam, Tiruchirappalli, Tamil Nadu 620006",
                "description": "The foremost of the 108 Divya Desams, set on an island surrounded by the sacred Kaveri and Kollidam rivers. Features the Rajagopuram rising 239.5 feet, one of Asia's tallest.",
                "opening_time": "06:00 AM",
                "closing_time": "09:00 PM",
                "dress_code": "Traditional South Indian temple dress code.",
                "history": "Spanning 156 acres with 7 concentric parikramas (prakaras) and 21 imposing gopurams. Celebrated continuously by all twelve Alvars.",
                "image_url": "https://images.unsplash.com/photo-1567157577867-05ccb1388e66?auto=format&fit=crop&w=1200&q=80",
                "banner_url": "https://images.unsplash.com/photo-1567157577867-05ccb1388e66?auto=format&fit=crop&w=1600&q=80",
                "contact_phone": "+91 431 243 2246",
                "contact_email": "ranganathar@srirangam.gov.demo",
                "is_featured": False
            }
        ]

        created_temples = []
        for t_info in temples_data:
            temple = Temple(**t_info)
            db.session.add(temple)
            created_temples.append(temple)
        db.session.commit()

        # 3. Add Darshan Slots for each Temple
        for temple in created_temples:
            slots = [
                DarshanSlot(
                    temple_id=temple.id,
                    slot_name="Morning Suprabhata & Ushakkala Slot",
                    start_time="06:00 AM",
                    end_time="08:30 AM",
                    max_capacity=200,
                    price_general=0.0,
                    price_special=100.0,
                    price_vip=300.0
                ),
                DarshanSlot(
                    temple_id=temple.id,
                    slot_name="Forenoon Nitya Darshan Slot",
                    start_time="09:00 AM",
                    end_time="11:30 AM",
                    max_capacity=250,
                    price_general=0.0,
                    price_special=100.0,
                    price_vip=300.0
                ),
                DarshanSlot(
                    temple_id=temple.id,
                    slot_name="Afternoon Uchikkala Seva Slot",
                    start_time="12:00 PM",
                    end_time="01:30 PM",
                    max_capacity=150,
                    price_general=0.0,
                    price_special=100.0,
                    price_vip=300.0
                ),
                DarshanSlot(
                    temple_id=temple.id,
                    slot_name="Evening Sayaratchai & Deeparadhana Slot",
                    start_time="05:00 PM",
                    end_time="07:30 PM",
                    max_capacity=300,
                    price_general=0.0,
                    price_special=150.0,
                    price_vip=350.0
                ),
                DarshanSlot(
                    temple_id=temple.id,
                    slot_name="Night Arthajama Darshan Slot",
                    start_time="08:00 PM",
                    end_time="09:15 PM",
                    max_capacity=120,
                    price_general=0.0,
                    price_special=100.0,
                    price_vip=250.0
                )
            ]
            for s in slots:
                db.session.add(s)

        # 4. Add Special Poojas for Temples
        poojas_data = [
            # Madurai Meenakshi
            {"temple_id": created_temples[0].id, "name": "Sri Lalitha Sahasranama Archana", "deity": "Goddess Meenakshi", "description": "Sacred chanting of the 1000 glorious names of the Divine Mother with fragrant kumkum and jasmine flowers for health, family prosperity, and wisdom.", "price": 108.0, "duration_mins": 30, "items_included": "Kumkum Prasadam, Jasmine garland, Vibhuti packet"},
            {"temple_id": created_temples[0].id, "name": "Maha Meenakshi-Sundareswarar Thirukalyanam Seva", "deity": "Meenakshi Amman & Sundareswarar", "description": "Witness the auspicious divine celestial wedding ceremony seeking marital harmony, long life, and remover of marital obstacles.", "price": 1500.0, "duration_mins": 90, "items_included": "Sacred Silk Angavastram, Special Laddu, Vibhuti, Kumkum, Blessed Coconut"},
            {"temple_id": created_temples[0].id, "name": "Swarna Pushpa Archana", "deity": "Goddess Meenakshi", "description": "Archana performed offering golden flowers to the deity with Vedic mantras for abundance and career growth.", "price": 501.0, "duration_mins": 45, "items_included": "Gold-leaf laminated blessed picture, Dry Fruits Prasadam"},

            # Tirupati Venkateswara
            {"temple_id": created_temples[1].id, "name": "Venkateswara Ashtottara Sata Namavali Archana", "deity": "Lord Balaji", "description": "Special 108 sacred name recitation invoking Lord Srinivasa's blessings for wealth, fortune, and peaceful mind.", "price": 151.0, "duration_mins": 25, "items_included": "Holy Akshata, TTD Style Big Laddu token, Tulasi Dal"},
            {"temple_id": created_temples[1].id, "name": "Nijapada Darshanam & Thirumanjanam Seva", "deity": "Lord Venkateswara", "description": "Sacred abhishekam of the holy feet of Lord Balaji with perfumed civet oil, milk, and camphor water.", "price": 750.0, "duration_mins": 60, "items_included": "Blessed Ghee Pouch, Pure Sandalwood paste, Special Prasadam"},
            {"temple_id": created_temples[1].id, "name": "Kalyanotsavam Seva", "deity": "Sri Malayappa Swamy & Sridevi-Bhudevi", "description": "Grand divine wedding ritual of Lord Malayappa with His consorts.", "price": 2000.0, "duration_mins": 120, "items_included": "Blouse piece, Kanduva, 2 Special Laddus, Vada"},

            # Thanjavur Brihadeeswarar
            {"temple_id": created_temples[2].id, "name": "Maha Rudrabhishekam to Peruvudaiyar", "deity": "Lord Shiva", "description": "Grand abhishekam with 11 holy substances including cow milk, honey, sugarcane juice, tender coconut water, and fragrant vibhuti.", "price": 650.0, "duration_mins": 60, "items_included": "Vibhuti packet, Bilva leaves, Panchamirtham"},
            {"temple_id": created_temples[2].id, "name": "Pradosha Kala Pooja", "deity": "Lord Shiva & Maha Nandi", "description": "Special twilight pooja performed on auspicious Pradosham days for relief from karmic debts and obstacles.", "price": 350.0, "duration_mins": 45, "items_included": "Pradosha Vibhuti, Sandal paste, Pongal prasadam"},

            # Rameswaram
            {"temple_id": created_temples[3].id, "name": "Maha Spatika Linga Darshanam & Abhishekam", "deity": "Lord Ramanathaswamy", "description": "Early morning sacred abhishekam to the revered holy crystal lingam installed in the sanctum.", "price": 250.0, "duration_mins": 35, "items_included": "Holy Teertham bottle, Vibhuti packet, Rudraksha"},
            {"temple_id": created_temples[3].id, "name": "22 Holy Teertha Snanam & Sankalpam", "deity": "Lord Rama & Shiva", "description": "Guided sacred holy bath in all 22 ancient mineral wells inside the temple precincts with Vedic priest sankalpam.", "price": 400.0, "duration_mins": 75, "items_included": "Purified Ganga jal bottle, Kumkum, Temple coin"},

            # Palani
            {"temple_id": created_temples[4].id, "name": "Vibhuti & Sandal Abhishekam (Sandana Kappu)", "deity": "Lord Murugan", "description": "Devotional sandal paste application over the Navapashanam idol followed by fragrant rosewater and milk abhishekam.", "price": 500.0, "duration_mins": 50, "items_included": "Original Palani Panchamirtham Jar (250g), Blessed Vibhuti"},
            {"temple_id": created_temples[4].id, "name": "Shanmuga Archana with Vel Samarpana", "deity": "Lord Dhandayuthapani", "description": "Recitation of Kanda Shasti Kavacham and Thiruppugazh with red oleander flowers and sacred spear offerings.", "price": 200.0, "duration_mins": 30, "items_included": "Vel copper locket, Panchamirtham pack"}
        ]

        for p_info in poojas_data:
            pooja = Pooja(**p_info)
            db.session.add(pooja)

        # 5. Temple Authentic Prasadams
        prasadams_data = [
            {
                "temple_id": created_temples[1].id, # Tirupati
                "name": "Tirumala Srivari Pure Ghee Laddu",
                "description": "The world-famous sacred temple laddu made with pure country cow ghee, premium gram flour, cashew nuts, raisins, cardamom, and edible diamond sugar candy (kalkandu).",
                "price": 50.0,
                "weight_grams": 175,
                "expiry_days": 10,
                "packaging_info": "Food-grade airtight sacred box with tamper-proof seal",
                "stock_quantity": 250,
                "image_url": "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=800&q=80"
            },
            {
                "temple_id": created_temples[4].id, # Palani
                "name": "Original Palani Panchamirtham",
                "description": "GI-tagged divine offering prepared according to the centuries-old traditional formula using mountain virupachi bananas, jaggery, pure cow ghee, honey, cardamom, and dry dates without water.",
                "price": 85.0,
                "weight_grams": 250,
                "expiry_days": 30,
                "packaging_info": "Hygienic sealed PET jar with Devaswom hologram",
                "stock_quantity": 180,
                "image_url": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80"
            },
            {
                "temple_id": created_temples[0].id, # Madurai
                "name": "Madurai Meenakshi Kovil Puliyodarai (Tamarind Rice)",
                "description": "Authentic temple-style sour and spicy tamarind rice tempered with roasted peanuts, sesame oil, curry leaves, and secret temple spice blend.",
                "price": 60.0,
                "weight_grams": 300,
                "expiry_days": 2,
                "packaging_info": "Biodegradable banana leaf wrapped inner pack with thermal outer foil",
                "stock_quantity": 120,
                "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80"
            },
            {
                "temple_id": created_temples[2].id, # Thanjavur
                "name": "Thanjavur Periya Kovil Sakkarai Pongal",
                "description": "Rich traditional sweet pongal prepared with raw samba rice, split yellow moong dal, dark organic jaggery, whole cashews fried in pure desi ghee, and fragrant crushed cardamom.",
                "price": 70.0,
                "weight_grams": 300,
                "expiry_days": 2,
                "packaging_info": "Sealed eco-friendly microwave-safe container",
                "stock_quantity": 110,
                "image_url": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=800&q=80"
            },
            {
                "temple_id": created_temples[7].id, # Srirangam
                "name": "Srirangam Kancheepuram Temple Idli Prasadam",
                "description": "Spiced cylindrical temple idli steamed in mantharai leaves, seasoned with crushed pepper, cumin seeds, ginger powder, and pure ghee.",
                "price": 80.0,
                "weight_grams": 350,
                "expiry_days": 2,
                "packaging_info": "Traditional mantharai leaf container with outer seal",
                "stock_quantity": 90,
                "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80"
            },
            {
                "temple_id": created_temples[5].id, # Guruvayur
                "name": "Guruvayur Paal Payasam (Sweet Milk Kheer)",
                "description": "Lord Krishna's favorite celestial dessert made by slow-cooking unpolished red rice in rich cow milk and sugar for several hours until pale pink and fragrant.",
                "price": 90.0,
                "weight_grams": 300,
                "expiry_days": 3,
                "packaging_info": "Spill-proof vacuum tub with cooling seal",
                "stock_quantity": 140,
                "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80"
            },
            {
                "temple_id": created_temples[3].id, # Rameswaram
                "name": "Sacred Rameswaram Vibhuti & Teertham Kit",
                "description": "Consecrated holy Bhasma (vibhuti) prepared from pure cow dung ash and scented with herbs, along with 22 Teertham holy water vial.",
                "price": 45.0,
                "weight_grams": 150,
                "expiry_days": 365,
                "packaging_info": "Velvet devotional pouch with sealed glass vial",
                "stock_quantity": 200,
                "image_url": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=800&q=80"
            }
        ]

        for pr_info in prasadams_data:
            prasadam = Prasadam(**pr_info)
            db.session.add(prasadam)

        # 6. Online Pooja Store Products
        products_data = [
            {
                "name": "Fresh Madurai Malli (Jasmine) Pooja Garland",
                "category": "Flowers & Garlands",
                "description": "Fragrant hand-strung Madurai Jasmine (Malli) garland with roses and bilva leaves, delivered fresh in temperature-controlled packaging.",
                "price": 180.0,
                "stock_quantity": 60,
                "image_url": "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=800&q=80",
                "rating": 4.9
            },
            {
                "name": "Sacred Brass Panchamukhi Deepam (5-Face Diya)",
                "category": "Lamps & Diyas",
                "description": "Heavy solid brass handcrafted traditional South Indian lamp with peacock crown, ideal for home altar, nitya pooja, and auspicious ceremonies.",
                "price": 750.0,
                "stock_quantity": 40,
                "image_url": "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?auto=format&fit=crop&w=800&q=80",
                "rating": 4.9
            },
            {
                "name": "Pure Bhimseni Pachha Camphor (Karpuram) - 100g",
                "category": "Camphor & Dhoop",
                "description": "100% pure organic edible-grade crystal camphor that burns cleanly without leaving black residue or smoke. Emits divine calming aroma.",
                "price": 140.0,
                "stock_quantity": 150,
                "image_url": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=800&q=80",
                "rating": 4.8
            },
            {
                "name": "Authentic Mysore Sandalwood Paste (Chandan) - 50g",
                "category": "Kumkum & Turmeric",
                "description": "Naturally extracted cooling sandalwood paste with therapeutic fragrance, pure for deity abhishekam and devotional tilakam.",
                "price": 160.0,
                "stock_quantity": 80,
                "image_url": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=800&q=80",
                "rating": 4.9
            },
            {
                "name": "Temple Grade Divine Kumkum & Kasthuri Manjal Duo",
                "category": "Kumkum & Turmeric",
                "description": "Sacred chemical-free crimson Roli Kumkum made with turmeric, lemon, and lime, paired with aromatic wild Kasthuri turmeric powder.",
                "price": 95.0,
                "stock_quantity": 120,
                "image_url": "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=800&q=80",
                "rating": 4.8
            },
            {
                "name": "All-in-One Daily Nitya Pooja Samagri Kit",
                "category": "Pooja Kits",
                "description": "Comprehensive devotional box containing 15 essential items: Akshata, Sandal tablets, Dhoop sticks, Cotton wicks, Camphor, Vibhuti, Kumkum, Turmeric, Betel nuts, and Pooja Bell.",
                "price": 499.0,
                "stock_quantity": 50,
                "image_url": "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?auto=format&fit=crop&w=800&q=80",
                "rating": 5.0
            },
            {
                "name": "Pure Desi Cow Ghee Pooja Diya Wicks (Pack of 50)",
                "category": "Lamps & Diyas",
                "description": "Pre-made organic cow ghee dipped cotton wicks for hassle-free morning and evening deeparadhana.",
                "price": 120.0,
                "stock_quantity": 100,
                "image_url": "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?auto=format&fit=crop&w=800&q=80",
                "rating": 4.7
            },
            {
                "name": "Handmade Natural Temple Sambrani Dhoop Cups (Pack of 12)",
                "category": "Camphor & Dhoop",
                "description": "Traditional cow dung based charcoal-free cups infused with pure loban, guggulu, and aromatic temple resins.",
                "price": 110.0,
                "stock_quantity": 90,
                "image_url": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=800&q=80",
                "rating": 4.8
            }
        ]

        for p_info in products_data:
            product = Product(**p_info)
            db.session.add(product)

        # 7. Add Devotee Reviews
        reviews_data = [
            {"temple_id": created_temples[0].id, "user_name": "Rajarajan Sundaram", "rating": 5, "comment": "Seamless darshan booking through DivineConnect! The QR ticket worked smoothly at the South Tower counter. Excellent initiative!"},
            {"temple_id": created_temples[0].id, "user_name": "Kavitha Narayanan", "rating": 5, "comment": "Received authentic Madurai Puliyodarai prasadam well packaged. Pure divine bliss at home!"},
            {"temple_id": created_temples[1].id, "user_name": "Venkatachalam S.", "rating": 5, "comment": "The Special Darshan slot reservation made our family pilgrimage with elderly parents peaceful and hassle free."},
            {"temple_id": created_temples[2].id, "user_name": "Dr. Ananya Natarajan", "rating": 5, "comment": "Majestic architecture and very well organized pooja timings. Booking the Rudrabhishekam was easy."}
        ]
        for r in reviews_data:
            review = Review(**r)
            db.session.add(review)

        db.session.commit()
        print("[DivineConnect] Database populated successfully with rich South Indian temples and devotional services!")

if __name__ == '__main__':
    from flask import Flask
    from config import Config
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        seed_all_data()
