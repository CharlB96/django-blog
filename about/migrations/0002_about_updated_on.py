# Generated by Django 4.2.7 on 2023-11-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
