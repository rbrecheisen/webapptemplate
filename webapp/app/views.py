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
def minio(request):
    if request.method == 'POST':
        client = MinioBackend().client
        client.fget_object('my-bucket', 'cancer.csv', 'cancer.csv')
        return redirect(f'/objects/')
    return render(request, 'minio.html', context={})


""" ------------------------------------------------------------------------
"""
def upload(request):
    pass


""" ------------------------------------------------------------------------
"""
def download(request, file_name):
    pass
