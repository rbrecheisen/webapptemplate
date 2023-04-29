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
"""
@login_required
def process_bucket_objects(request, bucket_name):    
    client = MinioBackend().client
    # todo: get form param "recursive_cbx"
    recursive = request.POST.get('recursive_cbx')
    if recursive == 'on':
        # we're dealing with scan folder
        bucket_objects = client.list_objects(bucket_name, recursive=True)
        # get list of scan folders
        scan_folders = []
        for bucket_object in bucket_objects:
            scan_folder = bucket_object.object_name.split('/')[1]
            if scan_folder not in scan_folders:
                scan_folders.append(scan_folder)
        print(scan_folders)
    else:
        # we're dealing with L3 images
        bucket_objects = client.list_objects(bucket_name)
        files = []
        for bucket_object in bucket_objects:
            files.append(bucket_object.object_name)
        print(files)
    return render(request, 'minio/bucket_objects.html', context={
        'bucket_name': bucket_name, 
        'bucket_objects': bucket_objects
        })
