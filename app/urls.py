from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
python from django.contrib.auth import views

urlpatterns=[
     url('^$',views.index,name = 'index'),
     url(r'^logout/$', views.logout, {"next_page": '/'}),
]