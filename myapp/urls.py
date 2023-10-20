from django.urls import path, include
from . import views

urlpatterns = [  
  path('', views.PrestamoView.as_view(), name='index'),
  path('register/', views.FormSaveView.as_view(), name='save'),
  path('<int:id>/update', views.FormUpdateView.as_view(), name='update'),
  path('delete/', views.DeletePrestamoView.as_view(), name='delete'),
]