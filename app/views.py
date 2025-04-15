from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/extract')
def extract():
    return render_template("extract.html")

@app.route('/products')
def extract():
    return render_template("products.html")

@app.route('/author')
def extract():
    return render_template("author.html")

@app.route('/product<id>')
def product(product_id:int):
    return render_template("product.html", product_id=product_id)