/**
 * DivineConnect - GitHub Pages Interactive Client Application
 * Provides 100% full-featured client-side persistence and interactivity on GitHub Pages.
 */

// 1. Initial Demonstration Data
const INITIAL_TEMPLES = [
    {
        id: 1,
        name: "Arulmigu Meenakshi Sundareswarar Temple",
        deity: "Goddess Meenakshi & Lord Sundareswarar (Shiva)",
        city: "Madurai",
        state: "Tamil Nadu",
        address: "Madurai Main, Madurai, Tamil Nadu 625001",
        description: "One of the greatest architectural masterpieces of South India, featuring 14 soaring gopurams encrusted with thousands of mythological figures. Revered for divine grace, arts, and cultural heritage.",
        opening_time: "05:00 AM",
        closing_time: "09:30 PM",
        dress_code: "Traditional Dhoti/Veshti for Men, Saree or Chudidhar for Women. Western wear prohibited.",
        image_url: "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 452 234 4360",
        featured: true
    },
    {
        id: 2,
        name: "Sri Venkateswara Swamy Temple",
        deity: "Lord Venkateswara / Balaji (Maha Vishnu)",
        city: "Tirupati",
        state: "Andhra Pradesh",
        address: "S Mada St, Tirumala, Tirupati, Andhra Pradesh 517504",
        description: "Perched atop the sacred Seven Hills of Seshachalam, this is the Kaliyuga Vaikuntam and one of the most visited pilgrimage destinations on earth, where Lord Srinivasa grants boons.",
        opening_time: "03:00 AM",
        closing_time: "11:30 PM",
        dress_code: "Traditional White Dhoti/Pancha for Men; Traditional Saree for Women.",
        image_url: "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 877 227 7777",
        featured: true
    },
    {
        id: 3,
        name: "Brihadeeswarar Temple (Thanjai Periya Kovil)",
        deity: "Lord Shiva (Peruvudaiyar / Brihadisvara)",
        city: "Thanjavur",
        state: "Tamil Nadu",
        address: "Membalam Rd, Balaganapathy Nagar, Thanjavur, Tamil Nadu 613007",
        description: "UNESCO World Heritage Site and pinnacle of Chola imperial granite architecture. Features a 216-foot vimana crowned by an 80-tonne single granite Kumbam stone.",
        opening_time: "06:00 AM",
        closing_time: "08:30 PM",
        dress_code: "Traditional Hindu attire. Footwear strictly prohibited beyond outer threshold.",
        image_url: "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 4362 274 476",
        featured: true
    },
    {
        id: 4,
        name: "Arulmigu Ramanathaswamy Temple",
        deity: "Lord Ramanathaswamy (Shiva - Jyotirlinga)",
        city: "Rameswaram",
        state: "Tamil Nadu",
        address: "Rameswaram Island, Ramanathapuram, Tamil Nadu 623526",
        description: "Famed for having the longest sculptured pillared corridor among Hindu temples and 22 sacred teerthams (holy wells) where pilgrims take ritual purificatory baths.",
        opening_time: "05:00 AM",
        closing_time: "09:00 PM",
        dress_code: "Devotees taking teertham bath must change into dry traditional attire inside sanctum.",
        image_url: "https://images.unsplash.com/photo-1544717302-de2939b7ef71?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 4573 221 223",
        featured: true
    },
    {
        id: 5,
        name: "Arulmigu Dhandayuthapani Swamy Temple",
        deity: "Lord Murugan (Bala Dhandayuthapani)",
        city: "Palani",
        state: "Tamil Nadu",
        address: "Giri Veedhi, Palani, Dindigul District, Tamil Nadu 624601",
        description: "One of the Six Holy Abodes (Arupadai Veedu) of Lord Murugan. The deity idol was consecrated by revered Siddha Bogar using Navapashanam (nine medicinal substances).",
        opening_time: "05:30 AM",
        closing_time: "09:30 PM",
        dress_code: "Traditional South Indian costume.",
        image_url: "https://images.unsplash.com/photo-1621644820613-333d1c442345?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 4545 242 236",
        featured: true
    },
    {
        id: 6,
        name: "Guruvayur Sri Krishna Temple",
        deity: "Lord Krishna (Guruvayurappan / Unnikrishnan)",
        city: "Guruvayur",
        state: "Kerala",
        address: "Guruvayur Devaswom, Thrissur, Kerala 680101",
        description: "Revered as the 'Bhuloka Vaikuntam'. The four-armed idol of Lord Vishnu/Krishna holds the conch, discus, mace, and lotus, and is bathed daily in holy water and milk.",
        opening_time: "03:00 AM",
        closing_time: "09:30 PM",
        dress_code: "Strict traditional Kerala costume: Mundu (Veshti) without shirt for men; Saree for women.",
        image_url: "https://images.unsplash.com/photo-1609137144822-421714856f67?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 487 255 6335",
        featured: false
    },
    {
        id: 7,
        name: "Kapaleeshwarar Temple",
        deity: "Lord Shiva (Kapaleeshwarar) & Karpagambal",
        city: "Chennai",
        state: "Tamil Nadu",
        address: "Vada Agrahara, Mylapore, Chennai, Tamil Nadu 600004",
        description: "Ancient Dravidian temple in the cultural heart of Mylapore, Chennai. Featuring a 120-foot rainbow gopuram, sacred temple tank, and vibrant Panguni Peruvizha.",
        opening_time: "06:00 AM",
        closing_time: "09:00 PM",
        dress_code: "Traditional Hindu devotional clothing.",
        image_url: "https://images.unsplash.com/photo-1616428255955-46eb61fa40a3?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 44 2464 1670",
        featured: false
    },
    {
        id: 8,
        name: "Sri Ranganathaswamy Temple",
        deity: "Lord Ranganatha (Reclining Maha Vishnu)",
        city: "Srirangam",
        state: "Tamil Nadu",
        address: "Srirangam, Tiruchirappalli, Tamil Nadu 620006",
        description: "The foremost of the 108 Divya Desams, set on an island surrounded by the sacred Kaveri and Kollidam rivers. Features the Rajagopuram rising 239.5 feet.",
        opening_time: "06:00 AM",
        closing_time: "09:00 PM",
        dress_code: "Traditional South Indian temple dress code.",
        image_url: "https://images.unsplash.com/photo-1567157577867-05ccb1388e66?auto=format&fit=crop&w=1200&q=80",
        phone: "+91 431 243 2246",
        featured: false
    }
];

const INITIAL_SLOTS = [
    { id: 1, name: "Morning Suprabhata Slot", time: "06:00 AM - 08:30 AM", capacity: 200, special_price: 100, vip_price: 300 },
    { id: 2, name: "Forenoon Nitya Darshan Slot", time: "09:00 AM - 11:30 AM", capacity: 250, special_price: 100, vip_price: 300 },
    { id: 3, name: "Afternoon Uchikkala Seva", time: "12:00 PM - 01:30 PM", capacity: 150, special_price: 100, vip_price: 300 },
    { id: 4, name: "Evening Sayaratchai & Deepam", time: "05:00 PM - 07:30 PM", capacity: 300, special_price: 150, vip_price: 350 },
    { id: 5, name: "Night Arthajama Darshan", time: "08:00 PM - 09:15 PM", capacity: 120, special_price: 100, vip_price: 250 }
];

const INITIAL_POOJAS = [
    { id: 1, temple_id: 1, name: "Sri Lalitha Sahasranama Archana", deity: "Goddess Meenakshi", price: 108, duration: 30, items: "Kumkum Prasadam, Jasmine garland, Vibhuti", desc: "Chanting of 1000 holy names of Divine Mother for health and prosperity." },
    { id: 2, temple_id: 1, name: "Maha Thirukalyanam Seva", deity: "Meenakshi & Sundareswarar", price: 1500, duration: 90, items: "Silk Angavastram, Special Laddu, Coconut", desc: "Witness the divine celestial wedding seeking marital harmony." },
    { id: 3, temple_id: 2, name: "Venkateswara Ashtottara Archana", deity: "Lord Balaji", price: 151, duration: 25, items: "Holy Akshata, TTD Big Laddu, Tulasi", desc: "108 sacred names invoking Lord Srinivasa's blessings." },
    { id: 4, temple_id: 2, name: "Kalyanotsavam Seva", deity: "Sri Malayappa Swamy", price: 2000, duration: 120, items: "Kanduva, 2 Laddus, Vada", desc: "Grand divine wedding ritual of Malayappa Swamy with His consorts." },
    { id: 5, temple_id: 3, name: "Maha Rudrabhishekam to Peruvudaiyar", deity: "Lord Shiva", price: 650, duration: 60, items: "Vibhuti packet, Bilva leaves, Panchamirtham", desc: "Grand abhishekam with 11 sacred Dravyas for peace and purification." },
    { id: 6, temple_id: 4, name: "22 Holy Teertha Snanam & Sankalpam", deity: "Lord Rama & Shiva", price: 400, duration: 75, items: "Ganga Jal bottle, Kumkum, Coin", desc: "Sacred purificatory bath in 22 ancient mineral wells with priest sankalpam." },
    { id: 7, temple_id: 5, name: "Sandana Kappu (Sandal Abhishekam)", deity: "Lord Murugan", price: 500, duration: 50, items: "Original Palani Panchamirtham (250g), Vibhuti", desc: "Devotional sandal paste application over the Navapashanam idol." }
];

const INITIAL_PRASADAMS = [
    { id: 1, temple_id: 2, name: "Tirumala Srivari Pure Ghee Laddu", price: 50, weight: 175, expiry: 10, img: "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=800&q=80", packaging: "Airtight sacred box with tamper seal", desc: "Famous temple laddu with pure ghee, gram flour, cashews, and diamond sugar candy." },
    { id: 2, temple_id: 5, name: "Original Palani Panchamirtham", price: 85, weight: 250, expiry: 30, img: "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80", packaging: "Sealed PET jar with Devaswom hologram", desc: "GI-tagged divine offering made with mountain bananas, jaggery, honey and cardamom." },
    { id: 3, temple_id: 1, name: "Madurai Meenakshi Kovil Puliyodarai", price: 60, weight: 300, expiry: 2, img: "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80", packaging: "Banana leaf wrapped with outer thermal foil", desc: "Authentic sour & spicy temple tamarind rice tempered with roasted peanuts." },
    { id: 4, temple_id: 3, name: "Thanjavur Periya Kovil Sakkarai Pongal", price: 70, weight: 300, expiry: 2, img: "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=800&q=80", packaging: "Sealed eco-friendly microwave container", desc: "Traditional sweet pongal with samba rice, moong dal, organic jaggery and pure ghee." }
];

const INITIAL_PRODUCTS = [
    { id: 1, name: "Fresh Madurai Malli (Jasmine) Garland", category: "Flowers & Garlands", price: 180, stock: 45, rating: 4.9, img: "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=800&q=80", desc: "Fragrant hand-strung Madurai jasmine garland delivered in cold freshness." },
    { id: 2, name: "Sacred Brass Panchamukhi Deepam (5-Face Diya)", category: "Lamps & Diyas", price: 750, stock: 30, rating: 4.9, img: "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?auto=format&fit=crop&w=800&q=80", desc: "Heavy solid brass South Indian lamp with peacock crown for home altar." },
    { id: 3, name: "Pure Bhimseni Pachha Camphor (100g)", category: "Camphor & Dhoop", price: 140, stock: 120, rating: 4.8, img: "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=800&q=80", desc: "100% pure organic edible-grade crystal camphor that burns without black residue." },
    { id: 4, name: "All-in-One Daily Nitya Pooja Samagri Kit", category: "Pooja Kits", price: 499, stock: 40, rating: 5.0, img: "https://images.unsplash.com/photo-1605647540924-852290f6b0d5?auto=format&fit=crop&w=800&q=80", desc: "15 essential items: Bell, Akshata, Sandal tablets, Dhoop, Wicks, Kumkum, Turmeric." }
];

// 2. State Management via LocalStorage
function getStore() {
    return {
        user: JSON.parse(localStorage.getItem('dc_user') || 'null'),
        cart: JSON.parse(localStorage.getItem('dc_cart') || '[]'),
        darshans: JSON.parse(localStorage.getItem('dc_darshans') || '[]'),
        poojas: JSON.parse(localStorage.getItem('dc_poojas') || '[]'),
        orders: JSON.parse(localStorage.getItem('dc_orders') || '[]')
    };
}

function saveStore(key, value) {
    localStorage.setItem(`dc_${key}`, JSON.stringify(value));
}

// Global active selection
let currentTempleId = 1;

// 3. Navigation & View Switcher
function switchView(viewName) {
    document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-link-divine').forEach(el => el.classList.remove('active'));

    const target = document.getElementById(`view-${viewName}`);
    if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    const navBtn = document.getElementById(`nav-link-${viewName}`);
    if (navBtn) navBtn.classList.add('active');

    // Specific view initializers
    if (viewName === 'cart') renderCartView();
    if (viewName === 'dashboard') renderDashboardView();
    if (viewName === 'admin') renderAdminView();
    if (viewName === 'temples') renderTemplesView();
}

// 4. View Renderers
function renderHomeView() {
    // Featured Temples Row
    const templesRow = document.getElementById('home-featured-temples-row');
    if (templesRow) {
        templesRow.innerHTML = INITIAL_TEMPLES.filter(t => t.featured).map(t => `
            <div class="col-lg-4 col-md-6">
                <div class="card-divine">
                    <div class="card-divine-img-wrap">
                        <img src="${t.image_url}" alt="${t.name}">
                        <span class="card-tag"><i class="bi bi-clock"></i> ${t.opening_time} - ${t.closing_time}</span>
                    </div>
                    <div class="card-divine-body">
                        <div class="card-location"><i class="bi bi-geo-alt-fill"></i> ${t.city}, ${t.state}</div>
                        <h4 class="card-divine-title">${t.name}</h4>
                        <div class="card-deity"><strong>Pradhana Deity:</strong> ${t.deity}</div>
                        <p class="small text-muted mb-3 flex-grow-1">${t.description.substring(0, 110)}...</p>
                        <div class="d-flex gap-2 pt-2 border-top">
                            <button onclick="openTempleDetail(${t.id})" class="btn btn-divine-outline flex-fill small py-2">Details</button>
                            <button onclick="openDarshanBooking(${t.id})" class="btn btn-divine-primary flex-fill small py-2">
                                <i class="bi bi-ticket-perforated"></i> Book Darshan
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');
    }

    // Prasadams Row
    const prasadamRow = document.getElementById('home-prasadams-row');
    if (prasadamRow) {
        prasadamRow.innerHTML = INITIAL_PRASADAMS.map(pr => `
            <div class="col-lg-3 col-sm-6">
                <div class="card-divine h-100">
                    <div class="card-divine-img-wrap" style="height: 180px;">
                        <img src="${pr.img}" alt="${pr.name}">
                        <span class="card-tag"><i class="bi bi-shield-check"></i> ${pr.expiry} Days Shelf Life</span>
                    </div>
                    <div class="card-divine-body">
                        <h5 class="fw-bold fs-6 mb-1 text-dark">${pr.name}</h5>
                        <p class="small text-muted mb-2 flex-grow-1">${pr.desc}</p>
                        <div class="d-flex justify-content-between align-items-center pt-2 border-top">
                            <div>
                                <span class="fs-5 fw-bold text-danger">₹${pr.price}</span>
                                <small class="text-muted d-block" style="font-size: 0.72rem;">${pr.weight}g pack</small>
                            </div>
                            <button onclick="addItemToCart('prasadam', ${pr.id})" class="btn btn-divine-primary btn-sm px-3">
                                <i class="bi bi-cart-plus"></i> Add
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');
    }
}

function renderTemplesView() {
    const grid = document.getElementById('temples-grid-row');
    if (!grid) return;
    grid.innerHTML = INITIAL_TEMPLES.map(t => `
        <div class="col-lg-4 col-md-6">
            <div class="card-divine">
                <div class="card-divine-img-wrap">
                    <img src="${t.image_url}" alt="${t.name}">
                    <span class="card-tag"><i class="bi bi-clock"></i> ${t.opening_time} - ${t.closing_time}</span>
                </div>
                <div class="card-divine-body">
                    <div class="card-location"><i class="bi bi-geo-alt-fill"></i> ${t.city}, ${t.state}</div>
                    <h4 class="card-divine-title">${t.name}</h4>
                    <div class="card-deity"><strong>Pradhana Deity:</strong> ${t.deity}</div>
                    <p class="small text-muted mb-3 flex-grow-1">${t.description.substring(0, 110)}...</p>
                    <div class="d-flex gap-2 pt-2 border-top">
                        <button onclick="openTempleDetail(${t.id})" class="btn btn-divine-outline flex-fill small py-2">View Details</button>
                        <button onclick="openDarshanBooking(${t.id})" class="btn btn-divine-primary flex-fill small py-2">
                            <i class="bi bi-ticket-perforated"></i> Book Darshan
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

function openTempleDetail(templeId) {
    currentTempleId = templeId;
    const t = INITIAL_TEMPLES.find(item => item.id === templeId) || INITIAL_TEMPLES[0];

    document.getElementById('detail-temple-name').textContent = t.name;
    document.getElementById('detail-temple-city').textContent = `${t.city}, ${t.state}`;
    document.getElementById('detail-temple-deity').innerHTML = `<strong>Pradhana Deity:</strong> ${t.deity}`;
    document.getElementById('detail-temple-timings').textContent = `${t.opening_time} – ${t.closing_time}`;
    document.getElementById('detail-temple-phone').textContent = t.phone;
    document.getElementById('detail-temple-desc').textContent = t.description;
    document.getElementById('detail-temple-dresscode').textContent = t.dress_code;
    document.getElementById('detail-temple-address').innerHTML = `<strong>Address:</strong><br>${t.address}<br><strong>Contact:</strong> ${t.phone}`;

    // Book buttons
    document.getElementById('btn-hero-book-darshan').onclick = () => openDarshanBooking(t.id);
    document.getElementById('btn-table-book-darshan').onclick = () => openDarshanBooking(t.id);
    document.getElementById('btn-sidebar-book-darshan').onclick = () => openDarshanBooking(t.id);

    // Slots
    document.getElementById('detail-slots-tbody').innerHTML = INITIAL_SLOTS.map(s => `
        <tr>
            <td class="fw-bold">${s.name}</td>
            <td><span class="badge bg-light text-dark border">${s.time}</span></td>
            <td class="text-success fw-bold">Free</td>
            <td class="text-danger fw-bold">₹${s.special_price}</td>
            <td class="text-primary fw-bold">₹${s.vip_price}</td>
        </tr>
    `).join('');

    // Poojas
    const templePoojas = INITIAL_POOJAS.filter(p => p.temple_id === t.id);
    const poojasToRender = templePoojas.length ? templePoojas : INITIAL_POOJAS.slice(0, 2);
    document.getElementById('detail-poojas-row').innerHTML = poojasToRender.map(p => `
        <div class="col-md-6">
            <div class="p-3 border rounded-3 h-100 d-flex flex-column" style="background: var(--color-cream); border-color: var(--color-gold-border) !important;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <h5 class="fw-bold text-dark fs-6 mb-0">${p.name}</h5>
                    <span class="badge bg-danger fs-6">₹${p.price}</span>
                </div>
                <div class="small text-muted mb-2">Deity: ${p.deity}</div>
                <p class="small text-muted mb-2 flex-grow-1">${p.desc}</p>
                <button onclick="openPoojaView(${t.id}, ${p.id})" class="btn btn-divine-primary btn-sm w-100 mt-2">Book Pooja</button>
            </div>
        </div>
    `).join('');

    switchView('temple-detail');
}

// 5. Darshan Booking Handlers
function openDarshanBooking(templeId) {
    currentTempleId = templeId;
    const t = INITIAL_TEMPLES.find(item => item.id === templeId) || INITIAL_TEMPLES[0];
    document.getElementById('book-darshan-temple-title').textContent = t.name;

    // Set date bounds
    const today = new Date().toISOString().split('T')[0];
    const dateInput = document.getElementById('darshan-input-date');
    dateInput.min = today;
    dateInput.value = today;

    // Slots select
    document.getElementById('darshan-input-slot').innerHTML = INITIAL_SLOTS.map(s => `
        <option value="${s.id}">${s.name} (${s.time})</option>
    `).join('');

    renderDevoteeRows();
    recalculateDarshanTotal();
    calculateRemainingSlotCapacity();

    switchView('darshan-book');
}

function calculateRemainingSlotCapacity() {
    const slotId = document.getElementById('darshan-input-slot').value;
    const date = document.getElementById('darshan-input-date').value;
    const store = getStore();

    const booked = store.darshans
        .filter(d => d.slot_id == slotId && d.date === date && d.status === 'Confirmed')
        .reduce((sum, d) => sum + d.devotee_count, 0);

    const remaining = Math.max(0, 185 - booked);
    const badge = document.getElementById('darshan-remaining-capacity');
    badge.textContent = `${remaining} tokens remaining for this slot`;
}

function renderDevoteeRows() {
    const count = parseInt(document.getElementById('darshan-input-count').value) || 1;
    const container = document.getElementById('devotee-rows-container');
    const store = getStore();
    const defaultName = store.user ? store.user.name : "Sundaramurthy S";

    let html = '';
    for (let i = 1; i <= count; i++) {
        html += `
        <div class="devotee-card-box">
            <div class="d-flex justify-content-between mb-2">
                <span class="fw-bold small text-dark"><i class="bi bi-person-fill text-danger"></i> Devotee ${i} ${i === 1 ? '(Primary)' : ''}</span>
                <span class="badge bg-light text-muted border">Pilgrim #${i}</span>
            </div>
            <div class="row g-2">
                <div class="col-md-5">
                    <label class="small text-muted mb-1">Full Name (as per Govt ID) *</label>
                    <input type="text" id="devotee-name-${i}" class="form-control form-control-sm" value="${i === 1 ? defaultName : 'Family Member ' + i}" required>
                </div>
                <div class="col-md-2 col-6">
                    <label class="small text-muted mb-1">Age *</label>
                    <input type="number" id="devotee-age-${i}" class="form-control form-control-sm" value="32" min="1" max="110" required>
                </div>
                <div class="col-md-2 col-6">
                    <label class="small text-muted mb-1">Gender *</label>
                    <select id="devotee-gender-${i}" class="form-select form-select-sm">
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                    </select>
                </div>
                <div class="col-md-3">
                    <label class="small text-muted mb-1">ID Proof *</label>
                    <select id="devotee-idtype-${i}" class="form-select form-select-sm">
                        <option value="Aadhaar Card">Aadhaar Card</option>
                        <option value="Voter ID">Voter ID</option>
                        <option value="Passport">Passport</option>
                    </select>
                </div>
            </div>
        </div>
        `;
    }
    container.innerHTML = html;
}

function recalculateDarshanTotal() {
    const catSelect = document.getElementById('darshan-input-category');
    const countSelect = document.getElementById('darshan-input-count');
    const selectedOpt = catSelect.options[catSelect.selectedIndex];
    const unitPrice = parseFloat(selectedOpt.getAttribute('data-price') || 0);
    const count = parseInt(countSelect.value) || 1;
    const total = unitPrice * count;

    document.getElementById('darshan-unit-display').textContent = `₹${unitPrice}`;
    document.getElementById('darshan-total-display').textContent = `₹${total}`;
}

function submitDarshanBooking() {
    const store = getStore();
    const count = parseInt(document.getElementById('darshan-input-count').value);
    const category = document.getElementById('darshan-input-category').value;
    const slotId = document.getElementById('darshan-input-slot').value;
    const slot = INITIAL_SLOTS.find(s => s.id == slotId) || INITIAL_SLOTS[0];
    const date = document.getElementById('darshan-input-date').value;
    const temple = INITIAL_TEMPLES.find(t => t.id === currentTempleId) || INITIAL_TEMPLES[0];

    const catSelect = document.getElementById('darshan-input-category');
    const unitPrice = parseFloat(catSelect.options[catSelect.selectedIndex].getAttribute('data-price') || 0);
    const total = unitPrice * count;

    const devotees = [];
    for (let i = 1; i <= count; i++) {
        devotees.push({
            name: document.getElementById(`devotee-name-${i}`).value,
            age: document.getElementById(`devotee-age-${i}`).value,
            gender: document.getElementById(`devotee-gender-${i}`).value,
            id_type: document.getElementById(`devotee-idtype-${i}`).value,
            id_num: "XXXX-XXXX-8421"
        });
    }

    const ref = "DC-DAR-" + Math.random().toString(36).substring(2, 8).toUpperCase();

    const booking = {
        ref: ref,
        temple_id: temple.id,
        temple_name: temple.name,
        temple_city: temple.city,
        temple_deity: temple.deity,
        slot_id: slot.id,
        slot_time: slot.time,
        date: date,
        category: category,
        devotee_count: count,
        total_amount: total,
        devotees: devotees,
        status: "Confirmed",
        created_at: new Date().toLocaleDateString('en-GB')
    };

    store.darshans.unshift(booking);
    saveStore('darshans', store.darshans);

    // Show printable ticket
    showTicketPass(booking);
}

function showTicketPass(b) {
    document.getElementById('ticket-temple-name').textContent = b.temple_name;
    document.getElementById('ticket-temple-location').textContent = `${b.temple_city}, South India`;
    document.getElementById('ticket-temple-deity').innerHTML = `<strong>Deity:</strong> ${b.temple_deity}`;
    document.getElementById('ticket-ref-code').textContent = b.ref;
    document.getElementById('ticket-date').textContent = b.date;
    document.getElementById('ticket-slot').textContent = b.slot_time;
    document.getElementById('ticket-category').textContent = b.category;
    document.getElementById('ticket-count').textContent = `${b.devotee_count} Devotee(s)`;
    document.getElementById('ticket-issued-at').textContent = `Issued: ${b.created_at}`;

    document.getElementById('ticket-devotees-tbody').innerHTML = b.devotees.map((d, idx) => `
        <tr>
            <td>${idx + 1}</td>
            <td class="fw-bold">${d.name}</td>
            <td>${d.age} yrs / ${d.gender}</td>
            <td>${d.id_type}</td>
            <td><code>${d.id_num}</code></td>
        </tr>
    `).join('');

    // Generate real QR Code
    const qrContainer = document.getElementById('ticket-qr-canvas');
    qrContainer.innerHTML = '';
    new QRCode(qrContainer, {
        text: `DIVINECONNECT|${b.ref}|${b.temple_name}|${b.date}|DEVOTEES:${b.devotee_count}`,
        width: 130,
        height: 130,
        colorDark: "#6E1212",
        colorLight: "#FAF6EF",
        correctLevel: QRCode.CorrectLevel.M
    });

    switchView('ticket-view');
}

// 6. Pooja Booking Handlers
function openPoojaView(templeId, poojaId = 1) {
    currentTempleId = templeId;
    const t = INITIAL_TEMPLES.find(item => item.id === templeId) || INITIAL_TEMPLES[0];
    document.getElementById('pooja-book-temple-title').textContent = t.name;

    const today = new Date().toISOString().split('T')[0];
    const dateInput = document.getElementById('pooja-input-date');
    dateInput.min = today;
    dateInput.value = today;

    const templePoojas = INITIAL_POOJAS.filter(p => p.temple_id === t.id);
    const poojasToUse = templePoojas.length ? templePoojas : INITIAL_POOJAS;

    document.getElementById('pooja-select-id').innerHTML = poojasToUse.map(p => `
        <option value="${p.id}" ${p.id === poojaId ? 'selected' : ''}>${p.name} (₹${p.price})</option>
    `).join('');

    handlePoojaChange();
    switchView('pooja-book');
}

function handlePoojaChange() {
    const pId = document.getElementById('pooja-select-id').value;
    const p = INITIAL_POOJAS.find(item => item.id == pId) || INITIAL_POOJAS[0];
    document.getElementById('pooja-info-box').innerHTML = `
        <strong>Description:</strong> ${p.desc}<br>
        <strong>Included:</strong> ${p.items} • Duration: ${p.duration} mins
    `;
    document.getElementById('pooja-dakshina-total').textContent = `₹${p.price}`;
}

function submitPoojaBooking() {
    const store = getStore();
    const pId = document.getElementById('pooja-select-id').value;
    const p = INITIAL_POOJAS.find(item => item.id == pId) || INITIAL_POOJAS[0];
    const temple = INITIAL_TEMPLES.find(t => t.id === currentTempleId) || INITIAL_TEMPLES[0];

    const ref = "DC-PJA-" + Math.random().toString(36).substring(2, 8).toUpperCase();
    const booking = {
        ref: ref,
        temple_name: temple.name,
        pooja_name: p.name,
        deity: p.deity,
        date: document.getElementById('pooja-input-date').value,
        slot: document.getElementById('pooja-input-slot').value,
        devotee_name: document.getElementById('pooja-devotee-name').value,
        gothram: document.getElementById('pooja-gothram').value,
        nakshatra: document.getElementById('pooja-nakshatra').value,
        rasi: document.getElementById('pooja-rasi').value,
        amount: p.price
    };

    store.poojas.unshift(booking);
    saveStore('poojas', store.poojas);

    // Show pooja pass
    document.getElementById('pass-pooja-name').textContent = booking.pooja_name;
    document.getElementById('pass-temple-name').textContent = booking.temple_name;
    document.getElementById('pass-temple-deity').innerHTML = `<strong>Presiding Deity:</strong> ${booking.deity}`;
    document.getElementById('pass-ref-code').textContent = booking.ref;
    document.getElementById('pass-date').textContent = booking.date;
    document.getElementById('pass-slot').textContent = booking.slot;
    document.getElementById('pass-amount').textContent = `₹${booking.amount}`;
    document.getElementById('pass-devotee-name').textContent = booking.devotee_name;
    document.getElementById('pass-gothram').textContent = booking.gothram;
    document.getElementById('pass-nakshatra').textContent = booking.nakshatra;
    document.getElementById('pass-rasi').textContent = booking.rasi;

    const qrContainer = document.getElementById('pass-qr-canvas');
    qrContainer.innerHTML = '';
    new QRCode(qrContainer, {
        text: `POOJA_PASS|${booking.ref}|${booking.temple_name}|${booking.devotee_name}|${booking.nakshatra}`,
        width: 130,
        height: 130,
        colorDark: "#6E1212",
        colorLight: "#FAF6EF",
        correctLevel: QRCode.CorrectLevel.M
    });

    switchView('pooja-pass');
}

// 7. Store & Cart Handlers
function renderStoreView() {
    const grid = document.getElementById('store-products-grid');
    if (!grid) return;
    grid.innerHTML = INITIAL_PRODUCTS.map(p => `
        <div class="col-lg-3 col-md-4 col-sm-6">
            <div class="card-divine h-100">
                <div class="card-divine-img-wrap" style="height: 200px;">
                    <img src="${p.img}" alt="${p.name}">
                    <span class="card-tag">⭐ ${p.rating}</span>
                </div>
                <div class="card-divine-body">
                    <span class="badge bg-light text-dark border small mb-1 align-self-start">${p.category}</span>
                    <h5 class="fw-bold fs-6 mb-1 text-dark">${p.name}</h5>
                    <p class="small text-muted mb-3 flex-grow-1">${p.desc}</p>
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="fs-5 fw-bold text-danger">₹${p.price}</span>
                        <span class="badge bg-success-subtle text-success small">In Stock</span>
                    </div>
                    <button onclick="addItemToCart('product', ${p.id})" class="btn btn-divine-primary btn-sm w-100">
                        <i class="bi bi-cart-plus"></i> Add to Cart
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

function renderPrasadamView() {
    const grid = document.getElementById('prasadams-grid');
    if (!grid) return;
    grid.innerHTML = INITIAL_PRASADAMS.map(pr => `
        <div class="col-lg-3 col-md-4 col-sm-6">
            <div class="card-divine h-100">
                <div class="card-divine-img-wrap" style="height: 200px;">
                    <img src="${pr.img}" alt="${pr.name}">
                    <span class="card-tag"><i class="bi bi-clock-history"></i> Shelf Life: ${pr.expiry}d</span>
                </div>
                <div class="card-divine-body">
                    <h5 class="fw-bold fs-6 mb-1 text-dark">${pr.name}</h5>
                    <p class="small text-muted mb-2 flex-grow-1">${pr.desc}</p>
                    <div class="small bg-light p-2 rounded border mb-3 text-muted" style="font-size: 0.75rem;">
                        <strong>Packaging:</strong> ${pr.packaging}
                    </div>
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <div>
                            <span class="fs-5 fw-bold text-danger">₹${pr.price}</span>
                            <small class="text-muted d-block">${pr.weight}g net</small>
                        </div>
                        <span class="badge bg-success-subtle text-success small">Fresh Daily</span>
                    </div>
                    <button onclick="addItemToCart('prasadam', ${pr.id})" class="btn btn-divine-primary btn-sm w-100">
                        <i class="bi bi-cart-plus"></i> Order Prasadam
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

function addItemToCart(type, id) {
    const store = getStore();
    let item = null;
    if (type === 'product') {
        const p = INITIAL_PRODUCTS.find(x => x.id === id);
        if (p) item = { type, id, name: p.name, price: p.price, img: p.img, qty: 1 };
    } else {
        const pr = INITIAL_PRASADAMS.find(x => x.id === id);
        if (pr) item = { type, id, name: pr.name, price: pr.price, img: pr.img, qty: 1 };
    }

    if (!item) return;

    const existing = store.cart.find(x => x.type === type && x.id === id);
    if (existing) {
        existing.qty += 1;
    } else {
        store.cart.push(item);
    }

    saveStore('cart', store.cart);
    updateCartBadge();
    showDevoteeToast(`Added "${item.name}" to your sacred cart!`);
}

function updateCartBadge() {
    const store = getStore();
    const count = store.cart.reduce((sum, item) => sum + item.qty, 0);
    const badge = document.getElementById('nav-cart-badge');
    if (badge) {
        badge.textContent = count;
        badge.style.display = count > 0 ? 'inline-block' : 'none';
    }
}

function renderCartView() {
    const store = getStore();
    const container = document.getElementById('cart-content-container');
    if (!container) return;

    if (!store.cart.length) {
        container.innerHTML = `
            <div class="text-center py-5 bg-white rounded-3 border">
                <div style="font-size: 4rem;">🛍️</div>
                <h3 class="temple-font mt-3">Your Devotional Cart is Empty</h3>
                <p class="text-muted small">Add authentic temple prasadams or blessed pooja store samagri to begin.</p>
                <div class="d-flex justify-content-center gap-2 mt-3">
                    <button onclick="switchView('prasadam')" class="btn btn-divine-primary px-3 py-2">Order Prasadam</button>
                    <button onclick="switchView('store')" class="btn btn-divine-gold px-3 py-2">Pooja Store</button>
                </div>
            </div>
        `;
        return;
    }

    const subtotal = store.cart.reduce((sum, item) => sum + item.price * item.qty, 0);
    const fee = subtotal >= 500 ? 0 : 40;
    const total = subtotal + fee;

    container.innerHTML = `
        <div class="row g-4">
            <div class="col-lg-7">
                <div class="bg-white p-4 rounded-3 border shadow-sm" style="border-color: var(--color-gold-border) !important;">
                    <h5 class="temple-font text-danger mb-3 border-bottom pb-2">Sacred Offerings (${store.cart.length} Items)</h5>
                    <div class="d-flex flex-column gap-3">
                        ${store.cart.map((item, idx) => `
                            <div class="p-3 border rounded-3 d-flex align-items-center gap-3" style="background: var(--color-cream-light);">
                                <img src="${item.img}" class="rounded" style="width: 60px; height: 60px; object-fit: cover;">
                                <div class="flex-grow-1">
                                    <h6 class="fw-bold mb-0 text-dark small">${item.name}</h6>
                                    <span class="text-danger fw-bold">₹${item.price}</span>
                                </div>
                                <div class="d-flex align-items-center gap-2">
                                    <button class="btn btn-sm btn-outline-secondary px-2 py-0" onclick="changeCartQty(${idx}, -1)">−</button>
                                    <span class="fw-bold">${item.qty}</span>
                                    <button class="btn btn-sm btn-outline-secondary px-2 py-0" onclick="changeCartQty(${idx}, 1)">+</button>
                                </div>
                                <div class="text-end" style="min-width: 60px;">
                                    <div class="fw-bold text-dark">₹${item.price * item.qty}</div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>

            <div class="col-lg-5">
                <div class="bg-white p-4 rounded-3 border shadow-sm" style="border-color: var(--color-gold-border) !important;">
                    <h5 class="temple-font text-danger mb-3 border-bottom pb-2">Delivery & Fulfillment</h5>
                    <form onsubmit="event.preventDefault(); processCheckout();">
                        <div class="mb-3">
                            <label class="form-label-divine">Recipient Name *</label>
                            <input type="text" id="chk-name" class="form-control form-control-sm" value="Sundaramurthy Swaminathan" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label-divine">Mobile Phone *</label>
                            <input type="tel" id="chk-phone" class="form-control form-control-sm" value="9840123456" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label-divine">Delivery Address *</label>
                            <input type="text" id="chk-address" class="form-control form-control-sm" value="42, Sannathi Street, Mylapore, Chennai" required>
                        </div>
                        <div class="p-3 rounded-3 border mb-3" style="background: var(--color-sand);">
                            <div class="d-flex justify-content-between small mb-1">
                                <span>Items Subtotal:</span>
                                <span class="fw-semibold">₹${subtotal}</span>
                            </div>
                            <div class="d-flex justify-content-between small mb-2">
                                <span>Packaging & Shipping:</span>
                                <span class="fw-semibold ${fee === 0 ? 'text-success' : ''}">${fee === 0 ? 'FREE' : '₹' + fee}</span>
                            </div>
                            <hr class="my-2">
                            <div class="d-flex justify-content-between">
                                <span class="fw-bold fs-6">Grand Total:</span>
                                <span class="fw-bold fs-4 text-danger">₹${total}</span>
                            </div>
                        </div>
                        <button type="submit" class="btn btn-divine-primary w-100 py-3 fw-bold">
                            <i class="bi bi-shield-lock-fill"></i> Pay ₹${total} & Place Order
                        </button>
                    </form>
                </div>
            </div>
        </div>
    `;
}

function changeCartQty(idx, delta) {
    const store = getStore();
    store.cart[idx].qty += delta;
    if (store.cart[idx].qty <= 0) {
        store.cart.splice(idx, 1);
    }
    saveStore('cart', store.cart);
    updateCartBadge();
    renderCartView();
}

function processCheckout() {
    const store = getStore();
    const subtotal = store.cart.reduce((sum, item) => sum + item.price * item.qty, 0);
    const fee = subtotal >= 500 ? 0 : 40;
    const total = subtotal + fee;

    const ref = "DC-ORD-" + Math.random().toString(36).substring(2, 8).toUpperCase();
    const order = {
        ref: ref,
        items: [...store.cart],
        total: total,
        name: document.getElementById('chk-name').value,
        phone: document.getElementById('chk-phone').value,
        address: document.getElementById('chk-address').value,
        status: "Confirmed",
        tracking: "TRK-" + Math.random().toString(36).substring(2, 8).toUpperCase(),
        date: new Date().toLocaleDateString('en-GB')
    };

    store.orders.unshift(order);
    store.cart = [];
    saveStore('orders', store.orders);
    saveStore('cart', store.cart);
    updateCartBadge();

    showDevoteeToast(`Order #${ref} placed successfully!`);
    switchView('dashboard');
}

// 8. Devotee Dashboard Renderers
function renderDashboardView() {
    const store = getStore();
    document.getElementById('dash-stat-darshans').textContent = store.darshans.length;
    document.getElementById('dash-stat-poojas').textContent = store.poojas.length;
    document.getElementById('dash-stat-orders').textContent = store.orders.length;

    // Darshans tbody
    const tbody = document.getElementById('dash-darshans-tbody');
    if (tbody) {
        if (!store.darshans.length) {
            tbody.innerHTML = `<tr><td colspan="7" class="text-center text-muted py-3">No darshan passes booked yet.</td></tr>`;
        } else {
            tbody.innerHTML = store.darshans.map((d, idx) => `
                <tr>
                    <td><span class="badge bg-light text-danger border fw-bold">${d.ref}</span></td>
                    <td class="fw-bold">${d.temple_name.split(' ').slice(0, 3).join(' ')}</td>
                    <td>${d.date} (${d.slot_time})</td>
                    <td>${d.category}</td>
                    <td>${d.devotee_count} Devotee(s)</td>
                    <td><span class="badge bg-success">${d.status}</span></td>
                    <td class="text-end">
                        <button onclick="viewSavedDarshan(${idx})" class="btn btn-outline-danger btn-sm">
                            <i class="bi bi-qr-code"></i> View Ticket
                        </button>
                    </td>
                </tr>
            `).join('');
        }
    }

    // Poojas tbody
    const poojasTbody = document.getElementById('dash-poojas-tbody');
    if (poojasTbody) {
        if (!store.poojas.length) {
            poojasTbody.innerHTML = `<tr><td colspan="7" class="text-center text-muted py-3">No pooja sevas booked yet.</td></tr>`;
        } else {
            poojasTbody.innerHTML = store.poojas.map(p => `
                <tr>
                    <td><span class="badge bg-light text-danger border fw-bold">${p.ref}</span></td>
                    <td class="fw-bold">${p.pooja_name}</td>
                    <td>${p.temple_name.split(' ').slice(0, 3).join(' ')}</td>
                    <td>${p.date} (${p.slot})</td>
                    <td>${p.devotee_name} (${p.nakshatra || 'Rohini'})</td>
                    <td class="fw-bold text-danger">₹${p.amount}</td>
                    <td class="text-end"><span class="badge bg-success">Confirmed</span></td>
                </tr>
            `).join('');
        }
    }

    // Orders
    const ordContainer = document.getElementById('dash-orders-container');
    if (ordContainer) {
        if (!store.orders.length) {
            ordContainer.innerHTML = `<p class="text-muted small mb-0">No prasadam or store orders placed yet.</p>`;
        } else {
            ordContainer.innerHTML = store.orders.map(o => `
                <div class="p-3 border rounded-3 mb-3" style="background: var(--color-cream-light);">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <span class="badge bg-danger fs-6">${o.ref}</span>
                        <span class="badge bg-success">${o.status}</span>
                    </div>
                    <div class="small text-muted mb-2">
                        <strong>Tracking ID:</strong> <code>${o.tracking}</code> • Total: <strong class="text-danger">₹${o.total}</strong>
                    </div>
                    <div class="p-2 bg-white rounded border small">
                        ${o.items.map(i => `${i.name} (x${i.qty})`).join(', ')}
                    </div>
                </div>
            `).join('');
        }
    }
}

function viewSavedDarshan(idx) {
    const store = getStore();
    if (store.darshans[idx]) {
        showTicketPass(store.darshans[idx]);
    }
}

// 9. Admin Portal Renderers
function renderAdminView() {
    const store = getStore();
    const darshanRevenue = store.darshans.reduce((sum, d) => sum + d.total_amount, 0);
    const poojaRevenue = store.poojas.reduce((sum, p) => sum + p.amount, 0);
    const orderRevenue = store.orders.reduce((sum, o) => sum + o.total, 0);
    const totalRev = darshanRevenue + poojaRevenue + orderRevenue + 12500;

    document.getElementById('admin-total-revenue').textContent = `₹${totalRev}`;
    document.getElementById('admin-darshan-count').textContent = store.darshans.length + 18;
    document.getElementById('admin-pooja-count').textContent = store.poojas.length + 12;
    document.getElementById('admin-orders-count').textContent = store.orders.length + 8;

    const tbody = document.getElementById('admin-darshan-tbody');
    if (tbody) {
        tbody.innerHTML = store.darshans.map(d => `
            <tr>
                <td><code>${d.ref}</code></td>
                <td class="fw-bold">${d.temple_name.split(' ').slice(0, 3).join(' ')}</td>
                <td>${d.date}</td>
                <td>${d.category}</td>
                <td>${d.devotee_count}</td>
                <td><span class="badge bg-success">${d.status}</span></td>
                <td><span class="badge bg-primary">Verified</span></td>
            </tr>
        `).join('') + `
            <tr>
                <td><code>DC-DAR-BALAJI</code></td>
                <td class="fw-bold">Sri Venkateswara Swamy</td>
                <td>Today</td>
                <td>VIP Sheegra</td>
                <td>2</td>
                <td><span class="badge bg-success">Confirmed</span></td>
                <td><span class="badge bg-primary">Turnstile Entry</span></td>
            </tr>
        `;
    }
}

// 10. Auth Modals & Helpers
function openLoginModal() {
    new bootstrap.Modal(document.getElementById('loginModal')).show();
}

function loginAs(role) {
    const user = {
        name: role === 'admin' ? "Temple Administrator" : "Sundaramurthy Swaminathan",
        email: role === 'admin' ? "admin@divineconnect.com" : "devotee@divineconnect.com",
        isAdmin: role === 'admin'
    };
    saveStore('user', user);
    bootstrap.Modal.getInstance(document.getElementById('loginModal')).hide();
    updateAuthUI();
    showDevoteeToast(`Welcome, ${user.name}!`);
    if (role === 'admin') {
        switchView('admin');
    } else {
        switchView('dashboard');
    }
}

function updateAuthUI() {
    const store = getStore();
    const container = document.getElementById('auth-nav-container');
    const adminPill = document.getElementById('dash-admin-pill');

    if (store.user) {
        container.innerHTML = `
            <div class="dropdown">
                <button class="btn btn-divine-primary dropdown-toggle rounded-pill px-3 py-2" data-bs-toggle="dropdown">
                    <i class="bi bi-person-circle"></i> ${store.user.name.split(' ')[0]}
                </button>
                <ul class="dropdown-menu dropdown-menu-end shadow border-warning">
                    <li><a class="dropdown-item py-2" href="javascript:void(0)" onclick="switchView('dashboard')"><i class="bi bi-speedometer2 text-danger me-2"></i> Devotee Dashboard</a></li>
                    ${store.user.isAdmin ? `<li><a class="dropdown-item py-2 fw-semibold text-warning-emphasis" href="javascript:void(0)" onclick="switchView('admin')"><i class="bi bi-shield-lock-fill text-warning me-2"></i> Admin Portal</a></li>` : ''}
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item py-2 text-danger" href="javascript:void(0)" onclick="logoutDevotee()"><i class="bi bi-box-arrow-right me-2"></i> Sign Out</a></li>
                </ul>
            </div>
        `;
        if (adminPill) adminPill.style.display = store.user.isAdmin ? 'block' : 'none';
    } else {
        container.innerHTML = `
            <button class="btn btn-divine-outline px-3 py-2" onclick="openLoginModal()">
                <i class="bi bi-person"></i> Sign In
            </button>
        `;
        if (adminPill) adminPill.style.display = 'none';
    }
}

function logoutDevotee() {
    localStorage.removeItem('dc_user');
    updateAuthUI();
    showDevoteeToast("Signed out successfully. Om Shanti.");
    switchView('home');
}

function showDevoteeToast(msg) {
    if (typeof showToast === 'function') {
        showToast(msg, 'success');
    }
}

function filterTemples() {
    const query = document.getElementById('filter-temple-name').value.toLowerCase();
    const city = document.getElementById('filter-temple-city').value.toLowerCase();

    const filtered = INITIAL_TEMPLES.filter(t => {
        const matchesQuery = t.name.toLowerCase().includes(query) || t.deity.toLowerCase().includes(query);
        const matchesCity = !city || t.city.toLowerCase() === city;
        return matchesQuery && matchesCity;
    });

    const grid = document.getElementById('temples-grid-row');
    if (!filtered.length) {
        grid.innerHTML = `<div class="col-12 text-center py-5"><h5 class="text-muted">No sacred temples matched your search.</h5></div>`;
    } else {
        grid.innerHTML = filtered.map(t => `
            <div class="col-lg-4 col-md-6">
                <div class="card-divine">
                    <div class="card-divine-img-wrap">
                        <img src="${t.image_url}" alt="${t.name}">
                        <span class="card-tag"><i class="bi bi-clock"></i> ${t.opening_time} - ${t.closing_time}</span>
                    </div>
                    <div class="card-divine-body">
                        <div class="card-location"><i class="bi bi-geo-alt-fill"></i> ${t.city}, ${t.state}</div>
                        <h4 class="card-divine-title">${t.name}</h4>
                        <div class="card-deity"><strong>Pradhana Deity:</strong> ${t.deity}</div>
                        <p class="small text-muted mb-3 flex-grow-1">${t.description.substring(0, 110)}...</p>
                        <div class="d-flex gap-2 pt-2 border-top">
                            <button onclick="openTempleDetail(${t.id})" class="btn btn-divine-outline flex-fill small py-2">View Details</button>
                            <button onclick="openDarshanBooking(${t.id})" class="btn btn-divine-primary flex-fill small py-2">
                                <i class="bi bi-ticket-perforated"></i> Book Darshan
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');
    }
}

function resetTempleFilters() {
    document.getElementById('filter-temple-name').value = '';
    document.getElementById('filter-temple-city').value = '';
    filterTemples();
}

function performHomeSearch() {
    const query = document.getElementById('home-search-query').value;
    const city = document.getElementById('home-search-city').value;
    switchView('temples');
    document.getElementById('filter-temple-name').value = query;
    document.getElementById('filter-temple-city').value = city;
    filterTemples();
}

// 11. Initializer on Load
document.addEventListener('DOMContentLoaded', () => {
    // Default initial mock user if empty
    const store = getStore();
    if (!store.user) {
        saveStore('user', { name: "Sundaramurthy Swaminathan", email: "devotee@divineconnect.com", isAdmin: false });
    }

    renderHomeView();
    renderTemplesView();
    renderStoreView();
    renderPrasadamView();
    updateCartBadge();
    updateAuthUI();
});
