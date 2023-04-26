from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_objects),
    path('objects/', views.get_objects),
    path('objects/create', views.create_object),
    path('objects/<int:obj_id>/', views.get_object),
    path('objects/<int:obj_id>/update', views.update_object),
    path('objects/<int:obj_id>/delete', views.delete_object),
    path('objects/<int:obj_id>/children/create', views.create_child),
    path('objects/<int:obj_id>/children/<int:child_id>/', views.get_child),
    path('objects/<int:obj_id>/children/<int:child_id>/update', views.update_child),
    path('objects/<int:obj_id>/children/<int:child_id>/delete', views.delete_child),
    path('minio/buckets/', views.get_buckets),
    path('minio/buckets/<str:bucket_name>/', views.get_bucket_objects),
    path('minio/buckets/<str:bucket_name>/', views.process_bucket_objects),
    # path('upload', views.upload),
    # path('download/<str:file_name>', views.download),
]