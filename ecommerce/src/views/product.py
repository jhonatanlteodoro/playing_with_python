from src.views.template_view import TemplateView



class ProductView(TemplateView):
    URL = "/product/<int:product_id>"
    TEMPLATE_NAME = "product_detail.html"
    METHOD = "GET"

    def run(self, **kwargs):
        return self.render_template(**{"product_id": kwargs.get("product_id")})
