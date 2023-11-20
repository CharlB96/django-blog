from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


class AboutList(generic.ListView):
    about = About.objects.all().order_by('-updated_on').first()
    template_name = "about/about.html"

def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate = collaborate_form.save(commit=False)
            collaborate.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )