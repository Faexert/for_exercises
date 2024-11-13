from django.views.generic.list import ListView # importing the ListView class from Django, which makes it easy to create views for displaying a list of objects.
from articles.models import Car


class CarView(ListView): # inheritance of a ListView with basic functionality for working with lists of objects
    model = Car
    queryset = Car.objects.all()
    template_name = 'home.html'
    context_object_name = 'cars_list'


