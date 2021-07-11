from django.urls import path
from . import views

urlpatterns=[
    path('upload_reason/',views.upload_reason,name='upload_reason'),
    path('delete_reason/<str:pk>/',views.delete_reason,name='delete_reason'),
    path('update_reason/<str:pk>/',views.update_reason,name='update_reason'),
    path('upload_reason/',views.upload_reason,name='upload_reason'),
    path('upload_comment/<str:pk>/',views.upload_comment,name='upload_comment'),
    path('',views.get_all_reasons,name='get_all_reasons'),
]