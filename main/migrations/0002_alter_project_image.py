# Generated by Django 4.2.5 on 2023-10-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='media/project_img/default.jpg', upload_to='media/project_img'),
        ),
    ]
