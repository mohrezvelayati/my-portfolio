# Generated by Django 4.2.5 on 2023-10-26 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]