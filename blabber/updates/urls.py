from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^statuses/all', views.all_statuses, name='all_statuses'),
    url(r'^statuses/new', views.new_status, name='new_status'),
    url(r'^statuses/favorite/(?P<status_id>\d+)$', views.add_favorite, name='add_favorite'),
    url(r'^statuses/unfavorite/(?P<status_id>\d+)$', views.remove_favorite, name='remove_favorite'),
    url(r'^statuses/(?P<status_id>\d+)$', views.status_detail, name='status_detail'),
    url(r'^$', views.recent_statuses, name='recent_statuses'),
    url(r'^user/(?P<user_id>\d+)$', views.show_user, name='user_detail'),
    url(r'^user/(?P<username>\S+)$', views.show_user_by_username),
]
