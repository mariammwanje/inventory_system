from allauth.account.views import LoginView
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^inventory/', include('inventory.urls', namespace='inventory')),
    #url(r'^accounts/', include('allauth.urls')),
    #url(r'^login/$', LoginView.as_view(), name='login'),

    #url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
]

urlpatterns += staticfiles_urlpatterns()
