import datetime
from django.shortcuts import render, redirect
from django.views import View
from .models import ConferenceRoom, RoomReservation


# Create your views here.
class MainPage(View):
    """
    Renders main page template.
    """

    def get(self, request):
        return render(request, 'main-page.html')


class AddRoom(View):
    """
    Renders template with form and added data provided by user to the database.
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
    """
    Takes all records from database and send it in context in rendered template.
    """

    def get(self, request):
        rooms = ConferenceRoom.objects.all()  # takes all data from database
        for room in rooms:
            reservation_dates = [reservation.date for reservation in
                                 room.roomreservation_set.all()]  # for each room take list of dates
            room.reserved = datetime.date.today() in reservation_dates  # checks if room is available today
        return render(request, "room-list.html", context={"rooms": rooms})


class DeleteRoom(View):
    """
    Deletes room from database by its id.
    """

    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        room.delete()
        return redirect("room-list")


class ModifyRoom(View):
    """
    Edits room by its id and save changes to database.
    """

    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        return render(request, 'edit-room.html', context={"room": room})

    def post(self, request, room_id):
        # gets data from form
        room = ConferenceRoom.objects.get(id=room_id)
        name = request.POST.get("name")
        capacity = int(request.POST.get("capacity"))
        projector = request.POST.get("projector") == "on"

        # checks if form is properly filled up
        if not name:
            return render(request, "edit-room.html", context={"error": "Name was not given", "room": room})
        if capacity <= 0:
            return render(request, "add-room.html",
                          context={"error": "Room capacity cant be less than 0", "room": room})
        if name != room.room_name and ConferenceRoom.objects.filter(
                room_name=name).first():  # checks if room with this name already exist
            return render(request, "add-room.html",
                          context={"error": "Room with this name already exist.", "room": room})

        # update records in database
        ConferenceRoom.objects.filter(id=room_id).update(room_name=name, room_capacity=capacity,
                                                         projector_availability=projector)
        return redirect("room-list")


class RoomReservations(View):
    """
    Renders template with form for room reservation,
    Checks inputs and create reservation in database.
    """

    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        reservations = room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, "room-reservation.html", context={"room": room, "reservations": reservations})

    def post(self, request, room_id):
        # takes data from form
        room = ConferenceRoom.objects.get(id=room_id)
        date = request.POST.get('reservation-date')
        comment = request.POST.get("comment")
        reservations = room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')

        # checks if date is set.
        if not date:
            return render(request, "room-reservation.html",
                          context={"room": room, "error": "Set a date!", "reservations": reservations})
        # checks if room isn't reserved.
        if RoomReservation.objects.filter(room_id=room, date=date):
            return render(request, "room-reservation.html",
                          context={"room": room, "error": "Room is already reserved", "reservations": reservations})
        # checks if date is not from past.
        if date < str(datetime.date.today()):
            return render(request, "room-reservation.html",
                          context={"room": room, "error": "Date is from the past", "reservations": reservations})

        RoomReservation.objects.create(room_id=room, date=date, comment=comment)
        return redirect("room-list")


class RoomDetails(View):
    """
    Renders template with room details.
    """

    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        reservations = room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, "room-details.html", context={"room": room, "reservations": reservations})
