# Generated by Django 4.2.7 on 2023-11-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_collaboraterequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='slug',
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='collaboraterequest',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
