from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.vid_up, name = 'video_upload'), 
]
