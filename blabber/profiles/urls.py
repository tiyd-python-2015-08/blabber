from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^edit', views.edit_profile, name='edit_profile'),
    url(r'^(?P<profile_id>\d+)$', views.profile_detail, name='profile_detail'),
    url(r'^(?P<profile_username>[\w\@\+\.\-]+)$', views.profile_detail, name='profile_detail_username')
]
