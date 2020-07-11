from django.urls import include, path

from .views import start, parents, schools

urlpatterns = [
    path('', start.home, name='home'),


]
