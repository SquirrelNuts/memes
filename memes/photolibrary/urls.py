from django.conf.urls import url
from . import views

app_name = 'photolibrary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
