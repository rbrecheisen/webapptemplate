# Generated by Django 4.2 on 2023-04-26 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('description', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildObjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.objectmodel')),
            ],
        ),
    ]
