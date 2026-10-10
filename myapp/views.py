from django.shortcuts import render

# Create your views here.
def my_page(request):
    context = {
        "name": "Кирилл Константинович",
        "age": 26,
        "bio": "Я работаю учителем и я учу ребят"
    }
    return render(request, "index.html", context)

def my_page2(request):
    context = {
        "name": "Константин Кириллович",
        "age": 62,
        "bio": "Я ненавижу детей и бью па башке чтобы ани ниче не знали"
    }
    return render(request, "index.html", context)
