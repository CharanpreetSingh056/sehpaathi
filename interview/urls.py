from django.urls import path
from . import views

urlpatterns=[

    path('',views.interview_experiences,name='interview_experiences'),
    path('new_interview_experience/',views.new_interview_experience,name='new_interview_experience'),
    path('delete_interview_experience/<str:pk>/',views.delete_interview_experience,name='delete_interview_experience'),
    path('update_interview_experience/<str:pk>/',views.update_interview_experience,name='update_interview_experience'),
    path('filter_interview_experiences/',views.filter_interview_experiences,name='filter_interview_experiences'),

]