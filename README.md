# Room-Reservation-System
Room Reservation System is a Django web application for making reservations of conference rooms with several functionalities such as:
  * [Rooms List](#rooms-list)
  * [Detailed View](#detailed-view)
  * [Add Room](#add-room)
  * [Edit Room](#edit-room)
  * [Room Reservation](#room-reservation)
  * [Search Room](#search-room) - in the future
  
  ### Rooms List
  List of all conference rooms taken from the database with their status (info if room is available that day or not). Next to their names link to edit, delete and reserve room.
  ### Detailed View
  As a user after clicking room's name you'll get detailed info about specific room - name, capacity, if it has projector or not. Additionaly info with dates when room is reserved. Also in this view you can edit, delet or reserve.
  ### Add Room
  Form for creating new room (name, capacity, projector availability). All data from form is added to the database after validation (Can't create room without name, with name that already exist or capacity that is less or equal 0).
  ### Edit Room
  You can edit and change (if needed) details about the room. Validation same as in Add Room. Database records are also udpated.
  ### Room Reservation
  After clicking "reserve" you'll be taken to web page where you can choose date of reservation and add comment. You will also see list of reservations of that room. Validation will not allow you to make reservation on date that is already taken. You will not be able to choose past dates. If everything went well reservation will be added to list and detailed info of that room.
  ### Search Room
  Implemented in the future
