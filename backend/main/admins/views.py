from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import UpcomingEvent

from .decorators import admin_required

User = get_user_model()

@admin_required
def home(request: HttpRequest) -> HttpResponse:
    upevents = []
    for obj in UpcomingEvent.objects.all():
        upevents.append({
            "title": obj.title,
            "desc": obj.description,
        })
    context = {'upevent': upevents}
    return render(request, 'admins/admins_home.html', context)

@admin_required
def admin_profile(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Admin Profile',
        'profile': True,
    }
    return render(request, 'admins/admins_profile.html', context)

@admin_required
def newupevent(request: HttpRequest) -> HttpResponse:
    if request.POST:
        title, desc = request.POST.get("title"), request.POST.get("desc")
        if len(title) == 0 or len(desc) == 0:
            messages.error(request, "Please Fill the form properly!")
        else:
            messages.info(request, f"Created new Post: {request.POST.get('title')}")
            got = UpcomingEvent.objects.create(title=title, description=desc, user=request.user)
            got.save()
            return redirect("admins-home")
    return render(request, 'admins/admins_newupevent.html')
