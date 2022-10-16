from django.conf.urls import url
from BookApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^book$',views.bookApi),
    url(r'^book/([0-9]+)$',views.bookApi),

]