from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def get_objects(request):
    pass


@login_required
def create_object(request):
    pass


@login_required
def get_object(request, object_id):
    pass


@login_required
def update_object(request, object_id):
    pass


@login_required
def delete_object(request, object_id):
    pass
