# Generated by Django 2.2.3 on 2019-11-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('willflyy', '0004_auto_20191105_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cr_date',
        ),
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(null=True, upload_to='profile_pics'),
        ),
    ]