from django.db import models


class ObjectModel(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, null=True)
    def __str__(self):
        return f'ObjectModel("{self.name}")'
    

class ChildObjectModel(models.Model):
    name = models.CharField(max_length=1024)
    obj = models.ForeignKey('ObjectModel', on_delete=models.CASCADE)
    def __str__(self):
        return f'ChildObjectModel("{self.name}", ObjectModel("{self.obj.name}"))'