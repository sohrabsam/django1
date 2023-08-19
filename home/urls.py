from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path("hello/", views.seyhello),
    path("d/<int:todo_id>", views.detile, name='ditle'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('update/<int:todo_id>', views.update, name='update'),

]
