-- =====================================================================
-- DivineConnect: MySQL Demonstration Seed Data
-- =====================================================================

USE `divineconnect`;

-- 1. Insert Admin & Devotee Users
-- Passwords hashed: admin123 and devotee123 (Werkzeug scrypt/pbkdf2 compatible)
INSERT INTO `users` (`id`, `name`, `email`, `password_hash`, `phone`, `address`, `city`, `state`, `pincode`, `nakshatra`, `rasi`, `gothra`, `is_admin`)
VALUES 
(1, 'DivineConnect Temple Admin', 'admin@divineconnect.com', 'scrypt:32768:8:1$uHkY8f1x$f622a55097495fce2a9756193796d1945a557b4f74d081512dbfb8a3068e64c489c670a5c4df1ec485d53ee39e557b4860b2eb391b1511c58c263c9b74301594', '9876543210', 'Devaswom Board Office, Anna Salai', 'Chennai', 'Tamil Nadu', '600002', 'Rohini', 'Vrishabha', 'Kashyapa', TRUE),
(2, 'Sundaramurthy Swaminathan', 'devotee@divineconnect.com', 'scrypt:32768:8:1$kM9L2q8v$b3d11b2cb01b44cbcf098495689104058d84458f2be52ad321588663806be44dcfb7c1fa7597bcbe7556a815330a1c1d0f592231b402cf97b102ce62aa213a4f', '9840123456', '42, Sannathi Street, Mylapore', 'Chennai', 'Tamil Nadu', '600004', 'Aswini', 'Mesham', 'Bharadwaja', FALSE);

-- 2. Insert Temples
INSERT INTO `temples` (`id`, `name`, `deity`, `city`, `state`, `address`, `description`, `opening_time`, `closing_time`, `dress_code`, `image_url`, `is_featured`, `is_active`)
VALUES
(1, 'Arulmigu Meenakshi Sundareswarar Temple', 'Goddess Meenakshi & Lord Sundareswarar', 'Madurai', 'Tamil Nadu', 'Madurai Main, Madurai, Tamil Nadu 625001', 'Architectural jewel of South India with 14 towering gopurams celebrating divine cosmic balance.', '05:00 AM', '09:30 PM', 'Traditional Veshti/Dhoti for Men, Saree or Chudidhar for Women', 'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80', TRUE, TRUE),
(2, 'Sri Venkateswara Swamy Temple', 'Lord Venkateswara / Balaji', 'Tirupati', 'Andhra Pradesh', 'S Mada St, Tirumala, Tirupati, Andhra Pradesh 517504', 'Kaliyuga Vaikuntam atop the sacred Seven Hills of Seshachalam.', '03:00 AM', '11:30 PM', 'Traditional White Dhoti/Pancha for Men; Saree for Women', 'https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80', TRUE, TRUE),
(3, 'Brihadeeswarar Temple (Thanjai Periya Kovil)', 'Lord Shiva (Peruvudaiyar)', 'Thanjavur', 'Tamil Nadu', 'Membalam Rd, Thanjavur, Tamil Nadu 613007', 'UNESCO World Heritage 1000-year-old granite temple built by Emperor Raja Raja Chola I.', '06:00 AM', '08:30 PM', 'Traditional Hindu attire', 'https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80', TRUE, TRUE),
(4, 'Arulmigu Ramanathaswamy Temple', 'Lord Ramanathaswamy (Jyotirlinga)', 'Rameswaram', 'Tamil Nadu', 'Rameswaram Island, Ramanathapuram, Tamil Nadu 623526', 'Longest pillared corridor in the world and 22 sacred teertham bathing points consecrated by Sri Rama.', '05:00 AM', '09:00 PM', 'Devotees taking teertha bath must wear dry clothes inside sanctum', 'https://images.unsplash.com/photo-1544717302-de2939b7ef71?auto=format&fit=crop&w=1200&q=80', TRUE, TRUE),
(5, 'Arulmigu Dhandayuthapani Swamy Temple', 'Lord Murugan', 'Palani', 'Tamil Nadu', 'Giri Veedhi, Palani, Tamil Nadu 624601', 'Abode of Bala Dhandayuthapani where deity was cast out of Navapashanam by Siddha Bogar.', '05:30 AM', '09:30 PM', 'Traditional South Indian attire', 'https://images.unsplash.com/photo-1621644820613-333d1c442345?auto=format&fit=crop&w=1200&q=80', TRUE, TRUE),
(6, 'Guruvayur Sri Krishna Temple', 'Lord Krishna (Guruvayurappan)', 'Guruvayur', 'Kerala', 'Guruvayur Devaswom, Thrissur, Kerala 680101', 'Bhuloka Vaikuntam of Kerala where four-armed Krishna is worshipped in divine infant form.', '03:00 AM', '09:30 PM', 'Mundu (Veshti) without shirt for men; Saree or Pavada for women', 'https://images.unsplash.com/photo-1609137144822-421714856f67?auto=format&fit=crop&w=1200&q=80', FALSE, TRUE);

-- 3. Insert Darshan Slots (For Temple 1 - Madurai Meenakshi)
INSERT INTO `darshan_slots` (`temple_id`, `slot_name`, `start_time`, `end_time`, `max_capacity`, `price_general`, `price_special`, `price_vip`)
VALUES
(1, 'Morning Suprabhata Slot', '06:00 AM', '08:30 AM', 200, 0.00, 100.00, 300.00),
(1, 'Forenoon Nitya Darshan Slot', '09:00 AM', '11:30 AM', 250, 0.00, 100.00, 300.00),
(1, 'Evening Sayaratchai Slot', '05:00 PM', '07:30 PM', 300, 0.00, 150.00, 350.00),
(2, 'Morning Suprabhata Slot', '06:00 AM', '08:30 AM', 200, 0.00, 100.00, 300.00),
(2, 'Forenoon Nitya Darshan Slot', '09:00 AM', '11:30 AM', 250, 0.00, 100.00, 300.00),
(2, 'Evening Sayaratchai Slot', '05:00 PM', '07:30 PM', 300, 0.00, 150.00, 350.00);

-- 4. Insert Products (Pooja Items Store)
INSERT INTO `products` (`name`, `category`, `description`, `price`, `stock_quantity`, `image_url`, `rating`)
VALUES
('Fresh Madurai Malli (Jasmine) Pooja Garland', 'Flowers & Garlands', 'Fragrant hand-strung Madurai Jasmine garland with fresh roses.', 180.00, 60, 'https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=800&q=80', 4.9),
('Sacred Brass Panchamukhi Deepam (5-Face Diya)', 'Lamps & Diyas', 'Solid brass traditional South Indian oil lamp with peacock crown.', 750.00, 40, 'https://images.unsplash.com/photo-1605647540924-852290f6b0d5?auto=format&fit=crop&w=800&q=80', 4.9),
('Pure Bhimseni Pachha Camphor (Karpuram) - 100g', 'Camphor & Dhoop', '100% pure organic crystal camphor burning smoke-free.', 140.00, 150, 'https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=800&q=80', 4.8),
('Authentic Mysore Sandalwood Paste (Chandan) - 50g', 'Kumkum & Turmeric', 'Naturally extracted sandalwood paste with cooling therapeutic aroma.', 160.00, 80, 'https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=800&q=80', 4.9),
('All-in-One Daily Nitya Pooja Samagri Kit', 'Pooja Kits', '15 essential devotional items including Bell, Akshata, Camphor, Wicks and Incense.', 499.00, 50, 'https://images.unsplash.com/photo-1605647540924-852290f6b0d5?auto=format&fit=crop&w=800&q=80', 5.0);

-- 5. Insert Prasadams
INSERT INTO `prasadams` (`temple_id`, `name`, `description`, `price`, `weight_grams`, `expiry_days`, `packaging_info`, `stock_quantity`, `image_url`)
VALUES
(2, 'Tirumala Srivari Pure Ghee Laddu', 'Sacred temple laddu made with pure cow ghee, gram flour, cashews, raisins, and cardamom.', 50.00, 175, 10, 'Airtight sacred box with tamper-proof seal', 250, 'https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=800&q=80'),
(5, 'Original Palani Panchamirtham', 'GI-tagged divine offering made with mountain bananas, jaggery, ghee, honey, and cardamom.', 85.00, 250, 30, 'Sealed PET jar with Devaswom hologram', 180, 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80'),
(1, 'Madurai Meenakshi Kovil Puliyodarai', 'Authentic temple tamarind rice tempered with roasted peanuts, curry leaves, and spices.', 60.00, 300, 2, 'Biodegradable banana leaf wrapped inner pack', 120, 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80'),
(3, 'Thanjavur Periya Kovil Sakkarai Pongal', 'Rich traditional sweet pongal with raw rice, yellow moong dal, jaggery, and cashews.', 70.00, 300, 2, 'Sealed eco-friendly microwave-safe container', 110, 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=800&q=80');
