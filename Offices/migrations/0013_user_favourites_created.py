# Generated by Django 2.2.2 on 2019-06-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offices', '0012_user_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_favourites',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
