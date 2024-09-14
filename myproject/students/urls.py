from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_list,name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
#     path('contact/',views.contact,name='contact'),
#     path('about/',views.about,name='about'),
 ]
