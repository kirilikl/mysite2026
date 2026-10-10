from django.shortcuts import render

# Create your views here.
def profile1(request):
    context = {
        "name": "Илья",
        "age": 67,
        "bio": "Инжинер строитель деревьев"
    }
    return render(request, "profile.html", context)

def music(request):
    return render(request, "music.html")