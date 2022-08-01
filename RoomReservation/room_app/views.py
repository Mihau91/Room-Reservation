from django.shortcuts import render, redirect
from django.views import View
from .models import ConferenceRoom


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

    def post(self, request):
        # gets data from form
        name = request.POST.get("name")
        capacity = int(request.POST.get("capacity"))

        projector = request.POST.get("projector") == "on"

        # checks if form is properly filled up
        if not name:
            return render(request, "add-room.html", context={"error": "Name was not given"})
        if capacity <= 0:
            return render(request, "add-room.html", context={"error": "Room capacity cant be less than 0"})
        if ConferenceRoom.objects.filter(room_name=name).first():  # checks if room with this name already exist
            return render(request, "add-room.html", context={"error": "Room with this name already exist."})

        # add room to database
        ConferenceRoom.objects.create(room_name=name, room_capacity=capacity, projector_availability=projector)
        return redirect("room-list")


class RoomList(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        return render(request, "room-list.html", context={"rooms": rooms-})
