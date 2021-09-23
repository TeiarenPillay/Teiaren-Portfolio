from django.urls import path
from . import views
# the app will come here when the url /blog has been requested
# Anything with /blog will be picked up from here

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # is there any path in this url that is an int
    path('<int:blog_id>/', views.detail, name='detail'),
]