from flask import render_template



class TemplateView:
    """
    This class is used to registry a view.
    It requires the method, url and handler name to be defined in order to initialize.
    """
    METHOD: str = None
    URL: str = None
    TEMPLATE_NAME: str = None

    def __init__(self) -> None:
        assert self.METHOD != None, "You must define the method value of your view"
        assert self.URL != None, "You must define the url value of your view"

    def render_template(self, **templete_args):

        return render_template(self.TEMPLATE_NAME, objects=templete_args)

    def run(self):
        raise NotImplemented("run was not implemented")




class TemplateAPIView:
    ...