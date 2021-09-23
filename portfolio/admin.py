# We specify what models we want to show up in our admin
from django.contrib import admin
from .models import Project

# This will put this model in admin
admin.site.register(Project)
