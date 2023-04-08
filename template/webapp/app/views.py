from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ObjectModel, ChildObjectModel


@login_required
def get_objects(request):
    objects = ObjectModel.objects.all()
    return render(request, 'objects.html', context={'objects': objects})


@login_required
def create_object(request):
    ObjectModel.objects.create(
        name=request.POST.get('name'), description=request.POST.get('description'))
    return redirect('/objects/')


@login_required
def get_object(request, obj_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    return render(request, 'object.html', context={'obj': obj})


@login_required
def update_object(request, obj_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    obj.name = request.POST.get('name')
    obj.description = request.POST.get('description')
    obj.save()
    return redirect(f'/objects/{obj_id}/')


@login_required
def delete_object(request, obj_id):
    obj = ObjectModel.objects.get(pk=obj_id)
    obj.delete()
    return redirect('/objects/')
