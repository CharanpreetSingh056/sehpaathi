from django.urls import path
from . import views

urlpatterns=[

    path('',views.get_all_questions,name='get_all_questions'),
    path('upload_question/',views.upload_question,name='upload_question'),
    path('delete_question/<str:pk>/',views.delete_question,name='delete_question'),
    path('update_question/<str:pk>/',views.update_question,name='update_question'),
    path('upload_answer/<str:pk>/',views.upload_answer,name='upload_answer'),

]