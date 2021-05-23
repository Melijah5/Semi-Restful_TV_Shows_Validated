from django.urls import path
from . import views

urlpatterns = [
      path('', views.index),
      path('new', views.new),
      path('<int:show_id>/edit' , views.edit),
      path('<int:show_id>', views.show),
      path('delete/<int:show_id>' , views.delete),
      
]
