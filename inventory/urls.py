from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='landing'),
    url(r'item/(?P<id>\d+)/$', views.item_detail, name='item_detail'),
    url(r'item/$', views.add_item, name='add-items'),
    url(r'help/$', views.help, name='help'),
    url(r'user_details$', views.users_details, name='user_details'),
]
