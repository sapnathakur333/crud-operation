
from django.urls import path

from .views import *


urlpatterns = [

    path(
        'signup/',
        signup_view,
        name='signup'
    ),

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        '',
        car_list,
        name='car_list'
    ),

    path(
        'create/',
        car_create,
        name='car_create'
    ),

    path(
        'edit/<int:id>/',
        car_edit,
        name='car_edit'
    ),

    path(
        'delete/<int:id>/',
        car_delete,
        name='car_delete'
    ),
]
