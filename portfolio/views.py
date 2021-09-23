import portfolio
from django.shortcuts import render
# this is an import to import the model for the model
# It will allow us to grab everything from project to use in this view
from .models import Project

def home(request):
    #grabs all the variables from the database that is from the projects 
    projects = Project.objects.all()
    # This will render to the view, reponse to the request/ calls the html template/ a dictionary that will pass all the information from projects into projects(dict) for the template to use
    return render (request, 'portfolio/home.html', { 'projects':projects })
