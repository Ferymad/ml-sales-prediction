from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS  # Import CORS
from .models import Sale  # Corrected import to reference the models module in the same package
from app import db  # Assuming you have initialized SQLAlchemy
from datetime import datetime  # Import datetime for date conversion

api = Blueprint('api', __name__)

# Enable CORS for the API
CORS(api)  # Apply CORS to the API blueprint

# Existing POST method for adding a sale
@api.route('/api/sales', methods=['POST'])
def add_sale():
    data = request.get_json()
    date_str = data.get('date')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    end_date_str = data.get('end_date')  # Get end_date from request

    # Convert date string to a date object
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None  # Convert if provided

    new_sale = Sale(date=date, product_id=product_id, quantity=quantity, end_date=end_date)
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({'message': 'Sale added successfully'}), 201

# New GET method for fetching sales data
@api.route('/api/sales', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    sales_list = [
        {
            'id': sale.id,
            'date': sale.date.strftime('%Y-%m-%d'),
            'product_id': sale.product_id,
            'quantity': sale.quantity,
            'end_date': sale.end_date.strftime('%Y-%m-%d') if sale.end_date else None,  # Include end_date
        }
        for sale in sales
    ]
    return jsonify(sales_list), 200

# Function to initialize routes
def init_routes(app):
    app.register_blueprint(api)
