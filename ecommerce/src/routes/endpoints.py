from flask import Blueprint
from src.views.product import ProductView
from src.views.home import HomeView


home_bp = Blueprint('home', __name__)
products_bp = Blueprint('product', __name__)


@home_bp.route(HomeView.URL, methods=[HomeView.METHOD])
def home(**kwargs):
    return HomeView().run(**kwargs)


@products_bp.route(ProductView.URL, methods=[ProductView.METHOD])
def product_detail(**kwargs):
    return ProductView().run(**kwargs)


def register_blueprint(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(products_bp)
    return
