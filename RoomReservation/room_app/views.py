from django.shortcuts import render
from django.views import View


# Create your views here.
class MainPage(View):
    """
    Renders main page template
    """
    def get(self, request):
        return render(request, 'main-page.html')
