from school import views
from django.urls import path, include
urlpatterns=[
    path('',views.home,name='home'),
    path('Login',views.Login,name='Login'),
    path('Registration',views.Registration,name='Registration'),
    path('rediectpage',views.rediectpage,name='rediectpage'),
    path('lastform', views.lastform, name='lastform'),
    path('lastfile', views.lastfile, name='lastfile'),
    path('logout', views.logout, name='logout'),

]