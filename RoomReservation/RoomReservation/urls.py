"""RoomReservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room_app.views import (
    MainPage,
    AddRoom,
    RoomList,
    DeleteRoom,
    ModifyRoom,
    RoomReservations,
    RoomDetails
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main-page'),
    path('room/new/', AddRoom.as_view(), name='add-room'),
    path('room/list/', RoomList.as_view(), name="room-list"),
    path('room/delete/<int:room_id>/', DeleteRoom.as_view(), name="delete-room"),
    path('room/modify/<int:room_id>/', ModifyRoom.as_view(), name="modify-room"),
    path('room/reserve/<int:room_id>/', RoomReservations.as_view(), name="room-reservation"),
    path('room/<int:room_id>/', RoomDetails.as_view(), name="room-details"),
]
