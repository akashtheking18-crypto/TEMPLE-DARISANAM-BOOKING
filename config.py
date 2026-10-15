import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'divine-connect-sacred-key-2026-south-temple')
    
    # MySQL Database configuration with SQLite fallback
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_PORT = os.environ.get('MYSQL_PORT', '3306')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'divineconnect')
    
    # Allow explicit DATABASE_URL override
    ENV_DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if ENV_DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = ENV_DATABASE_URL
    else:
        # Check if MySQL credentials are provided and MySQL is accessible
        # If MySQL connection fails, seamlessly use SQLite so the app runs out-of-the-box
        mysql_uri = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
        try:
            import pymysql
            # Quick check if MySQL server is responding (timeout 1.0s)
            conn = pymysql.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                port=int(MYSQL_PORT),
                connect_timeout=1
            )
            # Create database if it doesn't exist
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{MYSQL_DB}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            conn.close()
            SQLALCHEMY_DATABASE_URI = mysql_uri
            print(f"[DivineConnect] Connected to MySQL database '{MYSQL_DB}' successfully!")
        except Exception as e:
            # Fallback to local SQLite database
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'divineconnect.db')
            SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
            print(f"[DivineConnect] MySQL not running locally ({e}). Running on local SQLite DB: {db_path}")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Razorpay Test Credentials (can be configured via environment)
    RAZORPAY_KEY_ID = os.environ.get('RAZORPAY_KEY_ID', 'rzp_test_divineconnect2026')
    RAZORPAY_KEY_SECRET = os.environ.get('RAZORPAY_KEY_SECRET', 'divine_secret_test_key_sample')
    
    # App Settings
    APP_NAME = "DivineConnect"
    TAGLINE = "Smart Temple Booking & Devotional Services"
    CURRENCY = "₹"
    DEMO_MODE = True
