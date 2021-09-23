from django.db import models

class Project (models.Model): #inherits properties from the created django class that django created for us to take away the complexity of using a DB with web applications 
    # after models. refer to django documentation for what type of fields we can add
    title =  models.CharField(max_length=100)
    description =  models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) #blank is meaning you don't really need it 
    


