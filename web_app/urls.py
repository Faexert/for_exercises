from django.contrib import admin
from django.urls import path, include
#from django.views.generic import TemplateView
#from django.conf import settings

from articles.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'), # home page
    path('', CarView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('articles/', include('articles.urls')),
]
