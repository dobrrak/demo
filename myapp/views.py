from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse("hello world!")
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", { "todos": items})

def cv(request):

    paths = []
    for index in range(1,7):
        paths.append("resume/content" + str(index) + ".html")
    

    return render(request, "cv.html", {"paths": paths})