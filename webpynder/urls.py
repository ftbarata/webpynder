
from django.conf.urls import url
from django.contrib import admin
from .core.views import MainView, DetailView, NopeView, LikeView, burst_like, super_like_view

urlpatterns = [
    url(r'^$', MainView, name='main_view'),
    url(r'^detail/(?P<user_id>.*)$', DetailView, name='detail_view'),
    url(r'^burst/$', burst_like, name='burst_view'),
    url(r'^like/(?P<user_id>).*$', LikeView, name='like_view'),
    url(r'^superlike/(?P<user_id>).*$', super_like_view, name='super_like_view'),
    url(r'^nope/(?P<user_id>).*$', NopeView, name='nope_view'),
    url(r'^admin/', admin.site.urls),
]


