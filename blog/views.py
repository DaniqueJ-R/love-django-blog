from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_text(request):
    return HttpResponse("Hello, blog!")