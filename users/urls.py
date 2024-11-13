from django.urls import path, include # importing the path and include functions to configure routes in Django
from users.views import Register # register is a view class that will handle user registration

urlpatterns = [
    path('', include('django.contrib.auth.urls')), # standart tools

    path('register/', Register.as_view(), name='register'), # When navigating to the address /register/, the Register view will be called
]