from django.views.generic import  TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class Yield(TemplateView):
    template_name = "yield.html"

class Contacto(TemplateView):
    template_name = "contacto.html"

class PricesHistoric(TemplateView):
    template_name = "pricesHistoric.html"