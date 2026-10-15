import qrcode
import io
import base64
import random
import string
from functools import wraps
from flask import session, redirect, url_for, flash

def generate_qr_code_base64(data: str) -> str:
    """Generates a QR code and returns it as a base64 encoded data URI."""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=8,
            border=2,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#5a1818", back_color="#fff9f0") # Devotional maroon & cream colors
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return ""

def generate_reference_code(prefix: str = "DC") -> str:
    """Generates a distinct human-readable booking or order reference ID."""
    chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{chars}"

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in to access this devotional service.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Admin authentication required.", "danger")
            return redirect(url_for('login'))
        if not session.get('is_admin'):
            flash("Access denied. Admin privileges required.", "danger")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
