from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^contato/$',views.contato, name='contato'),
    url(r'^about/$',views.about, name='about'),
]
