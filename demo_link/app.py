from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 🗂️ Mock user portfolios
mock_portfolios = {
    101: {
        "username": "zaid_dev",
        "assets": [
            {"symbol": "AAPL", "quantity": 10, "price": 195.20},
            {"symbol": "MSFT", "quantity": 5, "price": 335.10},
            {"symbol": "INFY", "quantity": 12, "price": 1520.50}
        ]
    },
    102: {
        "username": "client_alpha",
        "assets": [
            {"symbol": "TSLA", "quantity": 3, "price": 712.55},
            {"symbol": "GOOG", "quantity": 2, "price": 2725.00}
        ]
    }
}

@app.route("/")
def home():
    return render_template("index.html", name="Zaid")

@app.route("/product")
def product_metadata():
    sample_product = {
        "product_id": 1,
        "name": "Oxford Shirt",
        "brand": "ClassicFit",
        "color": "Navy Blue",
        "size": "L",
        "material": "Cotton",
        "price": 1299.00,
        "stock_quantity": 25,
        "rating": 4.3,
        "available": True
    }
    return jsonify(sample_product)

@app.route("/portfolio/<int:user_id>")
def get_portfolio(user_id):
    user_data = mock_portfolios.get(user_id)

    if not user_data:
        return jsonify({"error": "User not found"}), 404

    total_value = sum(asset["quantity"] * asset["price"] for asset in user_data["assets"])

    return jsonify({
        "user_id": user_id,
        "username": user_data["username"],
        "assets": user_data["assets"],
        "total_value": round(total_value, 2),
        "last_updated": "2025-06-29 22:00 IST"
    })

if __name__ == "__main__":
    app.run(debug=True)


