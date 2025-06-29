CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    brand VARCHAR(50),
    category VARCHAR(50),
    color VARCHAR(30),
    size VARCHAR(10),
    material VARCHAR(50),
    price DECIMAL(10, 2),
    discount_percent DECIMAL(5, 2),
    stock_quantity INT,
    description TEXT,
    image_url TEXT,
    rating FLOAT,
    review_count INT,
    seller_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
