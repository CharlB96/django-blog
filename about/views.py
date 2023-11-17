from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

# Create your views here.


class AboutList(generic.ListView):
    about = About.objects.all().order_by('-updated_on').first()
    template_name = "about/about.html"

def about_me(request):
    """
    Display an individual :model:`blog.Post`.

    """

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )