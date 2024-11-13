from django.db import models

from users.models import User # importing User model to install a foreign key


# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=30) # car make
    model = models.CharField(max_length=60) # car model
    year = models.PositiveIntegerField() # year of creation of the car
    description = models.TextField() # car description
    created_at = models.DateTimeField(auto_now_add=True) # Date and time when the description was published
    updated_at = models.DateTimeField(auto_now=True) # Date and time when the description was changed
    owner = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)

    def __str__(self): #defining the __str__ method, which returns a string representation of the object
        return f'Make: {self.make} | Model: {self.model}'

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Date and time when the article was published
    car_id = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    author_id = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Author_id: {self.author_id}| Car_id: {self.car_id}'


