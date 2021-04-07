from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # db > monitor
    path('', views.home_page, name='home'),
    path('ajax_live_event_data', views.ajax_live_event_data, name='ajax_live_event_data'),
    path('event', views.event, name='event'),
    path('event/<event_id>', views.event, name='event'),
]
