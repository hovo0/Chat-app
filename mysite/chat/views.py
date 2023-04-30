from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, "chat/login.html")


@login_required
def room(request, room_name):
    username = request.user
    print(request)
    return render(request, "chat/room.html", {"room_name": room_name,
                                              "username": username})
