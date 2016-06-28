"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
admin.autodiscover()

from django.conf.urls import *
from test.view import hello
from test.testdb import testdb
from test import search
from test import search2

urlpatterns = patterns("",
	(r'^admin/', include(admin.site.urls)),
	('^hello/$', hello),
	('^testdb/$',testdb),
	(r'^search-form/$', search.search_form),
	(r'^search/$', search.search),
	(r'^search-post/$', search2.search_post),
)
