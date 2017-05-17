from django.conf.urls import url
from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create', views.create, name='create'),
    url(r'^(?P<todo_id>[0-9]+)/delete', views.delete, name='delete'),
    url(r'^(?P<todo_id>[0-9]+)/detail', views.detail, name='detail'),
    url(r'^(?P<todo_id>[0-9]+)/update', views.update, name='update')
]