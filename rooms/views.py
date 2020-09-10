from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 5, orphans=1)
    rooms = paginator.get_page(page)
    print(vars(rooms.paginator))
    return render(request, "rooms/home.html", {"page": rooms})
