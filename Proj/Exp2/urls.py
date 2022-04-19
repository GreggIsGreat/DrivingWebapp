from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('list_view/', views.list_view, name='list_view'),
    path('detail_view/<str:pk>/', views.detail_view,name='detail_view'),
    path('update/<str:pk>/',views.update, name='update'),
    path('register/', views.register, name='register'),
    path('neuralnet/', views.neuralnet, name='neuralnet')

]