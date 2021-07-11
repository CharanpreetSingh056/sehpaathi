from django.urls import path
from . import views

urlpatterns=[

    path('',views.homepage,name='homepage'),
    path('get_questions/',views.get_questions,name='get_questions'),
    path('new_question/',views.new_question,name='new_question'),
    path('delete_question/<str:pk>/',views.delete_question,name='delete_question'),
    path('update_question/<str:pk>/',views.update_question,name='update_question'),
    path('filter_questions/',views.filter_questions,name='filter_questions'),

]