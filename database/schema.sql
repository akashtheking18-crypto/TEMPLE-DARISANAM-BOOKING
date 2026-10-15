-- =====================================================================
-- DivineConnect: Smart Temple Booking & Devotional Services
-- MySQL Database Schema
-- Character Set: utf8mb4, Collation: utf8mb4_unicode_ci
-- =====================================================================

CREATE DATABASE IF NOT EXISTS `divineconnect` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `divineconnect`;

-- Drop existing tables in reverse dependency order if needed
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `reviews`;
DROP TABLE IF EXISTS `order_items`;
DROP TABLE IF EXISTS `orders`;
DROP TABLE IF EXISTS `prasadams`;
DROP TABLE IF EXISTS `products`;
DROP TABLE IF EXISTS `pooja_bookings`;
DROP TABLE IF EXISTS `poojas`;
DROP TABLE IF EXISTS `devotees`;
DROP TABLE IF EXISTS `darshan_bookings`;
DROP TABLE IF EXISTS `darshan_slots`;
DROP TABLE IF EXISTS `temples`;
DROP TABLE IF EXISTS `users`;
SET FOREIGN_KEY_CHECKS = 1;

-- 1. USERS TABLE
CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(120) NOT NULL,
    `email` VARCHAR(120) NOT NULL UNIQUE,
    `password_hash` VARCHAR(255) NOT NULL,
    `phone` VARCHAR(20) NULL,
    `address` VARCHAR(255) NULL,
    `city` VARCHAR(100) NULL,
    `state` VARCHAR(100) NULL,
    `pincode` VARCHAR(10) NULL,
    `nakshatra` VARCHAR(50) NULL,
    `rasi` VARCHAR(50) NULL,
    `gothra` VARCHAR(50) NULL,
    `is_admin` BOOLEAN DEFAULT FALSE,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. TEMPLES TABLE
CREATE TABLE `temples` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(150) NOT NULL,
    `deity` VARCHAR(100) NOT NULL,
    `city` VARCHAR(100) NOT NULL,
    `state` VARCHAR(100) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `description` TEXT NOT NULL,
    `opening_time` VARCHAR(50) DEFAULT '05:30 AM',
    `closing_time` VARCHAR(50) DEFAULT '09:00 PM',
    `dress_code` VARCHAR(255) DEFAULT 'Traditional Dhoti/Veshti for Men, Saree or Salwar for Women',
    `history` TEXT NULL,
    `image_url` VARCHAR(500) NULL,
    `banner_url` VARCHAR(500) NULL,
    `contact_phone` VARCHAR(50) NULL,
    `contact_email` VARCHAR(100) NULL,
    `is_featured` BOOLEAN DEFAULT FALSE,
    `is_active` BOOLEAN DEFAULT TRUE,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX `idx_temple_name` (`name`),
    INDEX `idx_temple_city` (`city`),
    INDEX `idx_temple_deity` (`deity`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. DARSHAN SLOTS TABLE
CREATE TABLE `darshan_slots` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `temple_id` INT NOT NULL,
    `slot_name` VARCHAR(100) NOT NULL,
    `start_time` VARCHAR(20) NOT NULL,
    `end_time` VARCHAR(20) NOT NULL,
    `max_capacity` INT DEFAULT 150,
    `price_general` DECIMAL(10, 2) DEFAULT 0.00,
    `price_special` DECIMAL(10, 2) DEFAULT 100.00,
    `price_vip` DECIMAL(10, 2) DEFAULT 300.00,
    `is_active` BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (`temple_id`) REFERENCES `temples`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. DARSHAN BOOKINGS TABLE
CREATE TABLE `darshan_bookings` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `booking_reference` VARCHAR(50) NOT NULL UNIQUE,
    `user_id` INT NOT NULL,
    `temple_id` INT NOT NULL,
    `slot_id` INT NOT NULL,
    `darshan_date` DATE NOT NULL,
    `category` VARCHAR(50) NOT NULL,
    `total_devotees` INT DEFAULT 1,
    `ticket_price` DECIMAL(10, 2) DEFAULT 0.00,
    `total_amount` DECIMAL(10, 2) DEFAULT 0.00,
    `payment_status` VARCHAR(30) DEFAULT 'Completed',
    `payment_id` VARCHAR(100) NULL,
    `qr_code_base64` LONGTEXT NULL,
    `status` VARCHAR(30) DEFAULT 'Confirmed',
    `cancellation_reason` VARCHAR(255) NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`temple_id`) REFERENCES `temples`(`id`),
    FOREIGN KEY (`slot_id`) REFERENCES `darshan_slots`(`id`),
    INDEX `idx_darshan_booking_ref` (`booking_reference`),
    INDEX `idx_darshan_slot_date` (`slot_id`, `darshan_date`, `status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. DEVOTEES TABLE (Individual tickets under a darshan booking)
CREATE TABLE `devotees` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `darshan_booking_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `age` INT NOT NULL,
    `gender` VARCHAR(20) NOT NULL,
    `id_type` VARCHAR(50) DEFAULT 'Aadhaar Card',
    `id_number` VARCHAR(50) NULL,
    FOREIGN KEY (`darshan_booking_id`) REFERENCES `darshan_bookings`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 6. POOJAS TABLE
CREATE TABLE `poojas` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `temple_id` INT NOT NULL,
    `name` VARCHAR(150) NOT NULL,
    `deity` VARCHAR(100) NOT NULL,
    `description` TEXT NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `duration_mins` INT DEFAULT 30,
    `items_included` VARCHAR(255) DEFAULT 'Flowers, Vibhuti, Kumkum, Prasadam Packet',
    `is_active` BOOLEAN DEFAULT TRUE,
    `image_url` VARCHAR(500) NULL,
    FOREIGN KEY (`temple_id`) REFERENCES `temples`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 7. POOJA BOOKINGS TABLE
CREATE TABLE `pooja_bookings` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `booking_reference` VARCHAR(50) NOT NULL UNIQUE,
    `user_id` INT NOT NULL,
    `temple_id` INT NOT NULL,
    `pooja_id` INT NOT NULL,
    `pooja_date` DATE NOT NULL,
    `time_slot` VARCHAR(50) NOT NULL,
    `devotee_name` VARCHAR(100) NOT NULL,
    `nakshatra` VARCHAR(50) NULL,
    `rasi` VARCHAR(50) NULL,
    `gothra` VARCHAR(50) NULL,
    `sankalpam_wish` TEXT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL,
    `payment_status` VARCHAR(30) DEFAULT 'Completed',
    `payment_id` VARCHAR(100) NULL,
    `qr_code_base64` LONGTEXT NULL,
    `status` VARCHAR(30) DEFAULT 'Confirmed',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`temple_id`) REFERENCES `temples`(`id`),
    FOREIGN KEY (`pooja_id`) REFERENCES `poojas`(`id`),
    INDEX `idx_pooja_booking_ref` (`booking_reference`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 8. PRODUCTS TABLE (Pooja Items Store)
CREATE TABLE `products` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(150) NOT NULL,
    `category` VARCHAR(100) NOT NULL,
    `description` TEXT NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `stock_quantity` INT DEFAULT 50,
    `image_url` VARCHAR(500) NULL,
    `rating` DECIMAL(3, 1) DEFAULT 4.8,
    `is_active` BOOLEAN DEFAULT TRUE,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX `idx_product_category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 9. PRASADAMS TABLE
CREATE TABLE `prasadams` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `temple_id` INT NOT NULL,
    `name` VARCHAR(150) NOT NULL,
    `description` TEXT NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `weight_grams` INT DEFAULT 250,
    `expiry_days` INT DEFAULT 7,
    `packaging_info` VARCHAR(200) DEFAULT 'Aroma-locked hygienic vacuum pouch',
    `stock_quantity` INT DEFAULT 100,
    `image_url` VARCHAR(500) NULL,
    `is_available` BOOLEAN DEFAULT TRUE,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`temple_id`) REFERENCES `temples`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 10. ORDERS TABLE (Unified for Store Products and Prasadam)
CREATE TABLE `orders` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `order_reference` VARCHAR(50) NOT NULL UNIQUE,
    `user_id` INT NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL,
    `delivery_type` VARCHAR(50) DEFAULT 'Doorstep Delivery',
    `pickup_temple_id` INT NULL,
    `shipping_name` VARCHAR(100) NOT NULL,
    `shipping_phone` VARCHAR(20) NOT NULL,
    `shipping_address` VARCHAR(255) NULL,
    `shipping_city` VARCHAR(100) NULL,
    `shipping_state` VARCHAR(100) NULL,
    `shipping_pincode` VARCHAR(10) NULL,
    `payment_status` VARCHAR(30) DEFAULT 'Completed',
    `payment_id` VARCHAR(100) NULL,
    `order_status` VARCHAR(50) DEFAULT 'Confirmed',
    `tracking_number` VARCHAR(100) NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`pickup_temple_id`) REFERENCES `temples`(`id`),
    INDEX `idx_order_ref` (`order_reference`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 11. ORDER ITEMS TABLE
CREATE TABLE `order_items` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `order_id` INT NOT NULL,
    `item_type` VARCHAR(20) NOT NULL,
    `product_id` INT NULL,
    `prasadam_id` INT NULL,
    `item_name` VARCHAR(150) NOT NULL,
    `unit_price` DECIMAL(10, 2) NOT NULL,
    `quantity` INT DEFAULT 1,
    `subtotal` DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (`order_id`) REFERENCES `orders`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`product_id`) REFERENCES `products`(`id`),
    FOREIGN KEY (`prasadam_id`) REFERENCES `prasadams`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 12. REVIEWS TABLE
CREATE TABLE `reviews` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `temple_id` INT NOT NULL,
    `user_name` VARCHAR(100) NOT NULL,
    `rating` INT DEFAULT 5,
    `comment` TEXT NOT NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`temple_id`) REFERENCES `temples`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
