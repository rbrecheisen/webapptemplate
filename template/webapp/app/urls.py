from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_objects),
    path('objects/', views.get_objects),
    path('objects/create', views.create_object),
    path('objects/<int:object_id>/', views.get_object),
    path('objects/<int:object_id>/update', views.update_object),
    path('objects/<int:object_id>/delete', views.delete_object),
    path('objects/<int:object_id>/children/', views.get_children),
    path('objects/<int:object_id>/children/create', views.create_child),
    path('objects/<int:object_id>/children/<int:child_id>/', views.get_child),
    path('objects/<int:object_id>/children/<int:child_id>/update', views.update_child),
    path('objects/<int:object_id>/children/<int:child_id>/delete', views.delete_child),
    path('upload', views.upload),
    path('download/<str:file_name>', views.download),
]