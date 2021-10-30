from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from .decorators import student_required

from admins.models import UpcomingEvent

User = get_user_model()

@student_required
def home(request: HttpRequest) -> HttpResponse:
    upevents = []
    for user in User.objects.all():
        if user.is_superuser:
            for obj in UpcomingEvent.objects.filter(user=user):
                upevents.append({
                    "username": user.username,
                    "title": obj.title,
                    "desc": obj.description
                })

    context = {"upevent": upevents}
    return render(request, 'students/home.html', context)

@student_required
def profile(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Student Profile',
        'profile': True,
    }
    return render(request, 'students/profile.html', context)

@student_required
def wishlist(request: HttpRequest) -> HttpResponse:
    return render(request, 'students/wishlist.html')

@student_required
def applied(request: HttpRequest) -> HttpResponse:
    return render(request, 'students/applied.html')