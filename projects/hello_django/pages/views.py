from django.http import HttpResponse
from django.views.generic import TemplateView


def home_page(request):
    return HttpResponse("Hello, Django!")


# Use template view to render HTML
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
