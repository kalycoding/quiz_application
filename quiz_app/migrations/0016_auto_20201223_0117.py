# Generated by Django 3.1.4 on 2020-12-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0015_auto_20201223_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz_time',
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_time',
            field=models.IntegerField(default=60),
        ),
    ]
