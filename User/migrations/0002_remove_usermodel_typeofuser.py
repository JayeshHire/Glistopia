# Generated by Django 4.1.7 on 2023-04-14 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='typeOfUser',
        ),
    ]
