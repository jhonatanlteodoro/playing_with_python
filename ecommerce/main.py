from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="src/templates")

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    return render_template('product_detail.html', product_id=product_id)
    # return f"<p>Product detail {product_id}</p>"