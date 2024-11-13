from django.contrib import admin # importing the admin module to have access to the Django admin panel
from django.contrib.auth import get_user_model # importing the get_user_model function to get the current user model used in the project
from django.contrib.auth.admin import UserAdmin # importing the standard UserAdmin from the Django authentication module to inherit the standard settings

User = get_user_model() # get the user model that is defined for the current project

@admin.register(User) # register the user model in the Django admin panel to manage users through the admin interface.
class UserAdmin(UserAdmin): # inheriting from the standard UserAdmin
    pass

