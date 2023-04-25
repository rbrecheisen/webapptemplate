from django.db import models
from django.dispatch import receiver


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


@receiver(models.signals.post_delete, sender=ChildObjectModel)
def child_object_post_delete(sender, instance, **kwargs):
    # import os
    # if os.path.isfile(instance.some_file):
    #     os.remove(instance.some_file)
    pass
