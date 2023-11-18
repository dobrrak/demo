from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse("hello world!")
    return render(request, "home.html")