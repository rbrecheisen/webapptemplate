from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_minio_backend import MinioBackend

from .models import ObjectModel, ChildObjectModel


""" ------------------------------------------------------------------------
"""
@login_required
def get_objects(request):
    objects = ObjectModel.objects.all()
    return render(request, 'objects.html', context={'objects': objects})


""" ------------------------------------------------------------------------
"""
@login_required
def create_object(request):
    ObjectModel.objects.create(
        name=request.POST.get('name'), description=request.POST.get('description'))
    return redirect('/objects/')


""" ------------------------------------------------------------------------
"""
@login_required
def get_object(request, obj_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    children = ChildObjectModel.objects.filter(obj=obj).all()
    return render(request, 'object.html', context={'obj': obj, 'children': children})


""" ------------------------------------------------------------------------
"""
@login_required
def update_object(request, obj_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    obj.name = request.POST.get('name')
    obj.description = request.POST.get('description')
    obj.save()
    return redirect(f'/objects/')


""" ------------------------------------------------------------------------
"""
@login_required
def delete_object(_, obj_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    obj.delete()
    return redirect('/objects/')


""" ------------------------------------------------------------------------
"""
@login_required
def create_child(request, obj_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    ChildObjectModel.objects.create(name=request.POST.get('name'), obj=obj)
    return redirect(f'/objects/{obj_id}/')


""" ------------------------------------------------------------------------
"""
@login_required
def get_child(request, obj_id, child_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    child = ChildObjectModel.objects.filter(obj=obj, pk=child_id).first()
    return render(request, 'child.html', context={'obj': obj, 'child': child})


""" ------------------------------------------------------------------------
"""
@login_required
def update_child(request, obj_id, child_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    child = ChildObjectModel.objects.filter(obj=obj, pk=child_id).first()
    child.name = request.POST.get('name')
    child.save()
    return redirect(f'/objects/{obj_id}/')


""" ------------------------------------------------------------------------
"""
@login_required
def delete_child(_, obj_id, child_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    child = ChildObjectModel.objects.filter(obj=obj, pk=child_id).first()
    child.delete()
    return redirect(f'/objects/{obj_id}/')


""" ------------------------------------------------------------------------
"""
@login_required
def get_buckets(request):
    client = MinioBackend().client
    buckets = client.list_buckets()
    return render(request, 'minio/buckets.html', context={'buckets': buckets})


""" ------------------------------------------------------------------------
"""
@login_required
def get_bucket_objects(request, bucket_name):
    client = MinioBackend().client
    bucket_objects = client.list_objects(bucket_name)
    return render(request, 'minio/bucket_objects.html', context={
        'bucket_name': bucket_name, 
        'bucket_objects': bucket_objects
        })


""" ------------------------------------------------------------------------
There are two scenario's: (1) The bucket contains a flat list of DICOM images
at L3 level or (2) the bucket contains a list of folders, each containing
DICOM images for a complete CT scan.

Question is how do we detect which scenario we are dealing with? In the first
scenario all images can be download to Mosamatic and processed. In the second
scenario each folder should be separately downloaded and processed before 
proceeding to the next folder. The previously downloaded folder should be 
deleted from Mosamatic.

We can use bucket tags for this purpose. In MinIO you can specify for each 
bucket a number of tags, e.g., "scans=true" to indicate the bucket contains
scan folders instead of only L3 images.
"""
@login_required
def process_bucket_objects(request, bucket_name):    
    client = MinioBackend().client
    tags = client.get_bucket_tags(bucket_name)
    if 'scans' in tags.keys():
        # processing bucket as list of scan folders
        pass
    else:
        # processing bucket as list of L3 images
        pass
    bucket_objects = client.list_objects(bucket_name)
    return render(request, 'minio/bucket_objects.html', context={
        'bucket_name': bucket_name, 
        'bucket_objects': bucket_objects
        })
