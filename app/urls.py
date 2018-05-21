from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^new/chapter$', views.new_chapter, name='new-chapter'),
    # url(r'^new/subject$', views.new_subject, name='new-subject'),
    url(r'^new/topic$', views.new_topic, name='new-chapter'),
    url(r'^new/content$', views.new_content, name='new-content'),
]