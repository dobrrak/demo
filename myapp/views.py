from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse("hello world!")
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", { "todos": items})

def cv(request):
    pages = [1, 2, 3, 4, 5, 6]
    return render(request, "cv.html", {"pages": pages})