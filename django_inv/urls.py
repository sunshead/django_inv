from django.conf.urls import include, url
from django.contrib import admin

from inventory import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_inv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'), #name group -- the digit characters will be called id
    url(r'^admin/', include(admin.site.urls)),
]
