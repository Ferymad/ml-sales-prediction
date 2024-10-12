# Define API routes
from flask import request, jsonify
from . import create_app
from .models import db, Product, Sale

app = create_app()

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.name for product in products])

@app.route('/api/sales', methods=['POST'])
def add_sale():
    data = request.json
    new_sale = Sale(product_id=data['product_id'], date=data['date'], quantity=data['quantity'])
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({'message': 'Sale added successfully'})
