from django.contrib import admin # importing the admin module to have access to the Django admin panel

from articles.models import Car, Comment # importing models from app

# register the Comment AND Car model in the Django admin panel.
admin.site.register(Car)
admin.site.register(Comment)