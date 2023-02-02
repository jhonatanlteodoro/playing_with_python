from src.views.template_view import TemplateView


class HomeView(TemplateView):
    URL = "/"
    TEMPLATE_NAME = "home.html"
    METHOD = "GET"

    def run(self, **kwargs):
        return self.render_template()
