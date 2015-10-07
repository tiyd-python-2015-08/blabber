from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^statuses/all', views.all_statuses),
    url(r'^statuses/', views.recent_statuses),
    url(r'^user/(?P<user_id>\d+)$', views.show_user),
    url(r'^user/(?P<username>\S+)$', views.show_user_by_username),
]
