from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('create/', views.add_documents, name='add-documents'),
    path('all/', views.view_documents, name='view_documents'),
    path('update/<int:pk>/', views.update_document, name='update-documents'),
    path('document/<int:pk>/delete/', views.delete_document, name='delete-documents'),
    path('document/<int:pk>/detail/', views.view_document, name='view-documents'),
    path('typification/create/', views.add_typification, name='add-typification'),
    path('typification/', views.view_typifications, name='view-typification'),

]
