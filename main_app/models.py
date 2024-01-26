from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
WORKS = (
    ('W', 'Warp Core'),
    ('S', 'Shields'),
    ('T', 'Transporters'),
)

class Starship(models.Model):
    name = models.CharField(max_length=100)
    registration = models.CharField(max_length=100)
    ship_class = models.CharField(max_length=100)
    captain = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'starship_id': self.id})
    
    def maintenance_today(self):
        # we can use django's filter, which produces a queryset for all feedings.
        # we'll look at the array(QuerySet) and compare it to the length of the MEALS tuple
        # we can return a boolean, that will be useful in our detail template
        return self.maintenance_set.filter(date=date.today()).count() >= len(WORKS)
    

class Maintenance(models.Model):
    # our model attributes go here
    # we can add a custom label to show up on our forms
    date = models.DateField('maintenance date')
    # meals are a charfield with max_length of one, because we're only going to save the first initial of each meal
    # this will help generate a dropdown in the automagically created modelform
    
    work = models.CharField(
        max_length=1,
        # add the custom 'choices' field option
        # this is what will create our dropdown menu
        choices=WORKS,
        # set the default choice, to be 'B'
        default=WORKS[0][0]
    )
    # creates the one to many relationship - Cat -< Feedings
    # models.ForeignKey needs two args, the model, and what to do if the parent model is deleted.
    # in the db, the column in the feedings table for the FK will be called cat_id, because django, by default, appends _id to the name of the model
    # DO NOT CONFUSE THIS WITH MONGODB AND THEIR `._id` NOT THE SAME
    starship = models.ForeignKey(Starship, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_work_display()} on {self.date} for {self.starship}"
    
    # change the default sort
    class Meta:
        ordering = ['-date']