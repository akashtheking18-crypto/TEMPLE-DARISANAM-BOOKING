/**
 * DivineConnect - Razorpay Test Payment Modal Simulation
 * Secure, clean, responsive test gateway modal supporting UPI, Cards, NetBanking.
 */

function initiatePayment(formId, amount, serviceName) {
    // If amount is 0 (e.g. Free Sarva Darshan), submit form directly
    if (amount <= 0) {
        document.getElementById(formId).submit();
        return;
    }

    // Check if modal already exists, else create it
    let modal = document.getElementById('razorpay-mock-modal');
    if (!modal) {
        const modalHtml = `
        <div class="modal fade" id="razorpay-mock-modal" tabindex="-1" aria-hidden="true" data-bs-backdrop="static">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content" style="border: 2px solid #C59B27; border-radius: 16px; overflow: hidden;">
                    <!-- Razorpay Header -->
                    <div style="background: linear-gradient(135deg, #0c2340 0%, #153e75 100%); color: white; padding: 20px;">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <div class="d-flex align-items-center gap-2">
                                <span style="font-size: 1.5rem;">🛕</span>
                                <div>
                                    <div style="font-weight: 700; font-size: 1.1rem; letter-spacing: 0.5px;">DivineConnect Gateway</div>
                                    <small style="color: #64B5F6; font-size: 0.75rem;">Razorpay Test Sandbox v2.4</small>
                                </div>
                            </div>
                            <span class="badge bg-warning text-dark px-2 py-1" style="font-size: 0.7rem; font-weight: 700;">TEST MODE</span>
                        </div>
                        <div class="d-flex justify-content-between align-items-end mt-3 pt-2" style="border-top: 1px solid rgba(255,255,255,0.15);">
                            <div>
                                <small style="color: #BBDEFB; display: block; font-size: 0.8rem;">Devotional Service</small>
                                <span id="rzp-service-name" style="font-weight: 600; font-size: 0.95rem;">Service</span>
                            </div>
                            <div class="text-end">
                                <small style="color: #BBDEFB; display: block; font-size: 0.8rem;">Amount Payable</small>
                                <span id="rzp-amount" style="font-size: 1.35rem; font-weight: 700; color: #FFE082;">₹0.00</span>
                            </div>
                        </div>
                    </div>

                    <!-- Payment Options Body -->
                    <div class="modal-body p-4" style="background: #FFFDF9;">
                        <p class="text-muted small mb-3">Select your preferred payment method:</p>
                        
                        <div class="list-group mb-4">
                            <!-- UPI -->
                            <label class="list-group-item list-group-item-action d-flex align-items-center gap-3 p-3 active" style="background: #FAF5EB; border-color: #E2C97C; color: #2A1A17; cursor: pointer;">
                                <input class="form-check-input flex-shrink-0" type="radio" name="rzp_method" value="upi" checked>
                                <span style="font-size: 1.3rem;">📱</span>
                                <div class="w-100">
                                    <div class="fw-bold">UPI / QR (Google Pay, PhonePe, Paytm, BHIM)</div>
                                    <small class="text-muted">Instant devotional payment via any UPI App</small>
                                </div>
                            </label>

                            <!-- Debit / Credit Card -->
                            <label class="list-group-item list-group-item-action d-flex align-items-center gap-3 p-3" style="cursor: pointer;">
                                <input class="form-check-input flex-shrink-0" type="radio" name="rzp_method" value="card">
                                <span style="font-size: 1.3rem;">💳</span>
                                <div class="w-100">
                                    <div class="fw-bold">Debit / Credit Card</div>
                                    <small class="text-muted">Visa, Mastercard, RuPay, Maestro</small>
                                </div>
                            </label>

                            <!-- Net Banking -->
                            <label class="list-group-item list-group-item-action d-flex align-items-center gap-3 p-3" style="cursor: pointer;">
                                <input class="form-check-input flex-shrink-0" type="radio" name="rzp_method" value="netbanking">
                                <span style="font-size: 1.3rem;">🏦</span>
                                <div class="w-100">
                                    <div class="fw-bold">Net Banking</div>
                                    <small class="text-muted">SBI, HDFC, ICICI, Canara, Indian Bank & more</small>
                                </div>
                            </label>
                        </div>

                        <!-- Processing Indicator -->
                        <div id="rzp-loader" class="text-center py-3" style="display: none;">
                            <div class="spinner-border text-danger mb-2" role="status"></div>
                            <div class="fw-bold text-dark">Securing Divine Blessing...</div>
                            <small class="text-muted">Confirming transaction with temple payment bridge</small>
                        </div>

                        <!-- Action Buttons -->
                        <div id="rzp-actions" class="d-flex gap-2">
                            <button type="button" class="btn btn-outline-secondary w-50" data-bs-dismiss="modal">Cancel</button>
                            <button type="button" class="btn btn-success w-50 fw-bold" id="rzp-pay-button" style="background: #2E7D32;">
                                Pay Now
                            </button>
                        </div>
                    </div>

                    <!-- Security Footer -->
                    <div class="text-center py-2" style="background: #F3EBDD; border-top: 1px solid #E2C97C; font-size: 0.75rem; color: #6B5B53;">
                        🔒 256-bit Encrypted SSL • Razorpay Verified Sandbox • RBI Compliant
                    </div>
                </div>
            </div>
        </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHtml);
        modal = document.getElementById('razorpay-mock-modal');
    }

    document.getElementById('rzp-service-name').textContent = serviceName;
    document.getElementById('rzp-amount').textContent = `₹${amount}`;

    const bsModal = new bootstrap.Modal(modal);
    bsModal.show();

    const payBtn = document.getElementById('rzp-pay-button');
    const loader = document.getElementById('rzp-loader');
    const actions = document.getElementById('rzp-actions');

    // Reset view
    loader.style.display = 'none';
    actions.style.display = 'flex';

    payBtn.onclick = function() {
        loader.style.display = 'block';
        actions.style.display = 'none';

        // Simulate 1.2s realistic gateway response
        setTimeout(() => {
            bsModal.hide();
            // Automatically submit the corresponding form
            document.getElementById(formId).submit();
        }, 1200);
    };
}
