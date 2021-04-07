from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # feeder
    path('', views.home_page, name='home'),
    path('generate_random_event', views.generate_random_event, name='generate_random_event'),

]
