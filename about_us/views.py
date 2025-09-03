from django.shortcuts import render
from .models import AboutUs
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    aboutus = AboutUs.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about_us.html",
        {"aboutus": aboutus,
         "collaborate_form": collaborate_form,},
    )
