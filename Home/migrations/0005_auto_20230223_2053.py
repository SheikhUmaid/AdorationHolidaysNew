# Generated by Django 3.2.13 on 2023-02-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20230223_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsubmit',
            name='mail_error',
            field=models.TextField(default='', max_length=50000),
        ),
        migrations.AddField(
            model_name='herosubmit',
            name='mail_error',
            field=models.TextField(default='', max_length=50000),
        ),
        migrations.AddField(
            model_name='modelsubmit',
            name='mail_error',
            field=models.TextField(default='', max_length=50000),
        ),
    ]
