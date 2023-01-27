from flask import Blueprint, render_template
from flask.views import MethodView

home_bp = Blueprint('home', __name__)
products_bp = Blueprint('product', __name__)


@home_bp.route("/")
def home():
    return render_template('home.html')


@products_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    return render_template('product_detail.html', product_id=product_id)