from django.contrib import admin


@admin.register
class ObjectModelAdmin(admin.ModelAdmin):
    list = (
        'name',
        'description',
    )


@admin.register
class ChildObjectModelAdmin(admin.ModelAdmin):
    list = (
        'name',
        'obj',
    )
