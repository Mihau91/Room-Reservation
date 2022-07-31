from django.shortcuts import render
from django.views import View


# Create your views here.
class MainPage(View):
    """
    Renders main page template
    """
    def get(self, request):
        return render(request, 'main-page.html')


class AddRoom(View):
    """
    Renders template with form and added data provided by user to the database
    """
    def get(self, request):
        return render(request, 'add-room.html')