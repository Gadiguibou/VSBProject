# Generated by Django 3.2.5 on 2021-08-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crn',
            name='class_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='crn',
            name='term',
            field=models.CharField(max_length=10, null=True),
        ),
    ]