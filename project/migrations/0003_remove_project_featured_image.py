# Generated by Django 3.2.18 on 2023-04-11 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='featured_image',
        ),
    ]
