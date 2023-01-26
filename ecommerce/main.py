from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    return f"<p>Product detail {product_id}</p>"