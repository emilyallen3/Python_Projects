from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    names = {'Nathan', 'Emily', 'Daniel', 'Eleanor', 'Audrey'}
    context = {
        'names': names,
    }
    return render(request, "home.html", context)