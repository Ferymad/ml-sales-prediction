# Define database models
from app import db  # Changed import to reference db from the new database module

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_code = db.Column(db.String(50), nullable=False)
    product_color = db.Column(db.String(50), nullable=True)
    product_model = db.Column(db.String(50), nullable=True)
    product_type = db.Column(db.String(50), nullable=True)

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)  # Ensure this field is optional
    quantity = db.Column(db.Integer, nullable=False)
