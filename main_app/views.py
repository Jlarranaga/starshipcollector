from django.shortcuts import render

from .models import Starship

# starships = [
#     {'name': 'USS Enterprise-D', 'registration' : 'NCC-1701-D', 'class': 'Galaxy', 'captain': 'Jean-Luc Picard'},
#     {'name': 'USS Voyager', 'registration': 'NCC-74656', 'class': 'Intrepid', 'captain': 'Catherine Janeway'},
#     {'name': 'USS Defiant', 'registration': 'NCC-75633', 'class': 'Defiant', 'captain': 'Benjamin Sisko'}
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def starships_index(request):
    # collect our objects from the database
    # this uses the objects object on the Cat model class
    # the objects object has a method called all
    # all grabs all of the entities using the parent model(in this case, Cat)
   
    # just like in ejs, we can pass some data to our views
    starships = Starship.objects.all()
    return render(request, 'starships/index.html', { 'starships': starships })

def starships_detail(request, starship_id):
    # find one cat with its id
    starship = Starship.objects.get(id=starship_id)

    return render(request, 'starships/detail.html', { 'starship': starship })