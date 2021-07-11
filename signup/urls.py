from django.urls import path
from . import views

urlpatterns=[

    path('',views.signup_page,name='signup_page'),
    path('signup_data/',views.signup_data,name='signup_data'),
    path('get_all/',views.getall,name='getall'),
    path('validation/<str:token>/',views.validate,name='validate'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('forgot_password_validate/<str:token>/',views.forgot_password_validate,name='forgot_password_validate.'),

]