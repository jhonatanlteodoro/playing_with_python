from flask import Flask
from src.routes.blueprints import home_bp, products_bp

app = Flask(__name__, template_folder="src/templates")
app.register_blueprint(home_bp)
app.register_blueprint(products_bp)
# @app.route("/")
# def home():
#     return render_template('home.html')


# @app.route("/product/<int:product_id>")
# def product_detail(product_id):
#     return render_template('product_detail.html', product_id=product_id)
#     # return f"<p>Product detail {product_id}</p>"