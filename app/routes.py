# Define API routes
from flask import request, jsonify
from . import create_app
from .models import db, Product, Sale
import joblib
import pandas as pd

app = create_app()

# Load the trained model
model = joblib.load('backend/app/ml/model.pkl')

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

@app.route('/api/predict', methods=['POST'])
def predict_sales():
    data = request.json
    # Assuming the input data is in the correct format expected by the model
    input_data = pd.DataFrame(data, index=[0])
    prediction = model.predict(input_data)
    return jsonify({'predicted_sales': prediction[0]})
