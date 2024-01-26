from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Starship
from .forms import MaintenanceForm

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
   
    starship = Starship.objects.get(id=starship_id)
    maintenance_form = MaintenanceForm()
    return render(request, 'starships/detail.html', { 'starship': starship, 'maintenance_form' : maintenance_form })

class StarshipCreate(CreateView):
    model = Starship
    fields='__all__'
    success_url = 'startships/{starship_id}'

# Update View - extends the UpdateView class
class StarshipUpdate(UpdateView):
    model = Starship
    # let's make it so you can't rename a cat
    # we could simply say fields = '__all__', or we can customize like this:
    fields = ['name', 'registration', 'ship_class', 'captain']

# Delete View - extends DeleteView
class StarshipDelete(DeleteView):
    model = Starship

    success_url = '/starships'

def add_maintenance(request, starship_id):
    # create a ModelForm instance using the data in request.POST
    form = MaintenanceForm(request.POST)
    # it's also important to validate forms.
    # django gives us a built in function for that
    if form.is_valid():
        # dont want to save the feeding to the db until we have a cat id
        new_maintenance = form.save(commit=False)
        # this is where we add the cat id
        new_maintenance.starship_id = starship_id
        new_maintenance.save()
    # finally, redirect to the cat detail page
    return redirect('detail', starship_id=starship_id)
