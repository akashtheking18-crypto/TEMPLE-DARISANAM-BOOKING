/**
 * DivineConnect - Core Frontend Interactivity
 */

// Cart Toast Notification
function showToast(message, type = 'success') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.position = 'fixed';
        container.style.bottom = '24px';
        container.style.right = '24px';
        container.style.zIndex = '99999';
        container.style.display = 'flex';
        container.style.flexDirection = 'column';
        container.style.gap = '10px';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    const bgClass = type === 'success' ? '#2e7d32' : (type === 'danger' ? '#c62828' : '#e65100');
    toast.style.background = bgClass;
    toast.style.color = '#fff';
    toast.style.padding = '12px 20px';
    toast.style.borderRadius = '8px';
    toast.style.boxShadow = '0 4px 15px rgba(0,0,0,0.2)';
    toast.style.fontSize = '0.9rem';
    toast.style.fontWeight = '500';
    toast.style.display = 'flex';
    toast.style.alignItems = 'center';
    toast.style.gap = '8px';
    toast.style.transition = 'opacity 0.3s ease';
    toast.innerHTML = `<span>🪔</span> <span>${message}</span>`;

    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 3200);
}

// Add Item to Sacred Cart (Products & Prasadam)
async function addToCart(itemType, itemId, quantity = 1) {
    try {
        const response = await fetch('/api/cart/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                item_type: itemType,
                item_id: itemId,
                quantity: parseInt(quantity) || 1
            })
        });

        const data = await response.json();
        if (data.success) {
            showToast(data.message, 'success');
            // Update cart badge across navbar
            const badges = document.querySelectorAll('.cart-badge-count');
            badges.forEach(b => {
                b.textContent = data.cart_count;
                b.style.display = data.cart_count > 0 ? 'inline-block' : 'none';
            });
        } else {
            showToast(data.message || 'Could not add item to cart', 'danger');
        }
    } catch (err) {
        console.error('Cart error:', err);
        showToast('Network error adding to cart', 'danger');
    }
}

// Update Cart Item Quantity
async function updateCartQty(cartKey, qty) {
    try {
        const response = await fetch('/api/cart/update', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cart_key: cartKey, quantity: parseInt(qty) })
        });
        const data = await response.json();
        if (data.success) {
            location.reload();
        }
    } catch (e) {
        console.error(e);
    }
}

// Remove Item from Cart
async function removeCartItem(cartKey) {
    if (!confirm('Remove this sacred offering from your cart?')) return;
    try {
        const response = await fetch('/api/cart/remove', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cart_key: cartKey })
        });
        const data = await response.json();
        if (data.success) {
            location.reload();
        }
    } catch (e) {
        console.error(e);
    }
}

// Check Darshan Availability dynamically on Booking page
async function checkSlotAvailability() {
    const slotSelect = document.getElementById('slot_id');
    const dateInput = document.getElementById('darshan_date');
    const availBadge = document.getElementById('slot-availability-badge');
    const remainingCountSpan = document.getElementById('remaining-count');
    const submitBtn = document.getElementById('btn-confirm-darshan');

    if (!slotSelect || !dateInput || !slotSelect.value || !dateInput.value) return;

    try {
        const response = await fetch(`/api/darshan/availability?slot_id=${slotSelect.value}&date=${dateInput.value}`);
        const data = await response.json();

        if (data.is_available) {
            availBadge.className = 'alert alert-success d-flex align-items-center justify-content-between p-2';
            availBadge.style.display = 'flex';
            remainingCountSpan.textContent = `${data.remaining_capacity} tokens remaining for this slot`;
            if (submitBtn) submitBtn.disabled = false;
        } else {
            availBadge.className = 'alert alert-danger d-flex align-items-center justify-content-between p-2';
            availBadge.style.display = 'flex';
            remainingCountSpan.textContent = `Housefull (0 tokens remaining). Please pick another slot or date.`;
            if (submitBtn) submitBtn.disabled = true;
        }

        updateDarshanSummary();
    } catch (err) {
        console.error('Availability check error:', err);
    }
}

// Devotee count handler to render devotee fields
function handleDevoteeCountChange() {
    const countSelect = document.getElementById('devotee_count');
    if (!countSelect) return;
    const count = parseInt(countSelect.value) || 1;

    for (let i = 1; i <= 6; i++) {
        const row = document.getElementById(`devotee-row-${i}`);
        if (row) {
            if (i <= count) {
                row.style.display = 'block';
                const reqInputs = row.querySelectorAll('input');
                reqInputs.forEach(inp => inp.required = true);
            } else {
                row.style.display = 'none';
                const reqInputs = row.querySelectorAll('input');
                reqInputs.forEach(inp => inp.required = false);
            }
        }
    }
    updateDarshanSummary();
}

// Calculate darshan booking total amount
function updateDarshanSummary() {
    const countSelect = document.getElementById('devotee_count');
    const catSelect = document.getElementById('category');
    const priceDisplay = document.getElementById('darshan-unit-price');
    const totalDisplay = document.getElementById('darshan-total-price');

    if (!countSelect || !catSelect) return;

    const count = parseInt(countSelect.value) || 1;
    const category = catSelect.value;
    
    // Read price from data attributes on option
    const selectedOpt = catSelect.options[catSelect.selectedIndex];
    const unitPrice = parseFloat(selectedOpt.getAttribute('data-price') || 0);

    const total = count * unitPrice;

    if (priceDisplay) priceDisplay.textContent = `₹${unitPrice}`;
    if (totalDisplay) totalDisplay.textContent = `₹${total}`;
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    // Attach listener to darshan form if present
    const slotSelect = document.getElementById('slot_id');
    const dateInput = document.getElementById('darshan_date');
    const countSelect = document.getElementById('devotee_count');
    const catSelect = document.getElementById('category');

    if (slotSelect) slotSelect.addEventListener('change', checkSlotAvailability);
    if (dateInput) dateInput.addEventListener('change', checkSlotAvailability);
    if (countSelect) countSelect.addEventListener('change', handleDevoteeCountChange);
    if (catSelect) catSelect.addEventListener('change', updateDarshanSummary);

    // Initial trigger
    if (slotSelect && dateInput && slotSelect.value && dateInput.value) {
        checkSlotAvailability();
    }
    if (countSelect) {
        handleDevoteeCountChange();
    }
});
