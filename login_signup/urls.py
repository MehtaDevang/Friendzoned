from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^signup', views.signup, name = 'signup'),
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^check_login', views.check_login, name='check_login'),
    url(r'^homepage', views.homepage, name='homepage'),
    url(r'^logout', views.logout, name = 'logout'),
    url(r'^send_request', views.send_request, name='send_request'),
    url(r'^accept_request', views.accept_request, name='accept_request'),
    url(r'^send_message', views.send_message, name='send_message'),
    url(r'^add_post', views.add_post, name='add_post'),
    url(r'^add_comment', views.add_comment, name='add_comment'),
]