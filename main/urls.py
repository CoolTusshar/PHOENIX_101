from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name = 'home'),
    url(r'^signup/$',views.signup,name = 'signup'),
    url(r'^feedback$',views.feedback,name = 'feedback'),
    url(r'^schools_near/$',views.map_school,name = 'map')
]