# Generated by Django 3.2.13 on 2022-07-18 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_snippet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
