from django.urls import path
from . import views

urlpatterns=[
	path('',views.index, name='index'),
	path('list', views.list),  
	path('delete_item/<int:item_id>/', views.delete_item)
]