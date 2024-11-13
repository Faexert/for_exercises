from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect # importing the render and redirect functions for rendering HTML templates and redirecting users
from users.forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html' # specify the template that will be used for the registration page

    def get(self, request): # GET request handler
        context = {
            'form': UserCreationForm()  # creating a new instance of the registration form and adding it to the context
        }
        return render(request, self.template_name, context) # displaying the registration page by passing the form to the template

    def post(self, request): # POST request handler
        form = UserCreationForm(request.POST) # creating an instance of the form with the data entered by the user

        if form.is_valid():
            form.save() # save new user in db
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # in the inline form password1
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = { # if the form is filled out incorrectly, we pass the form with errors back to the template
            'form' : form
        }
        return render(request, self.template_name, context) # showing errors
