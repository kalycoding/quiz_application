# Generated by Django 3.1.4 on 2020-12-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0025_auto_20201226_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='time_taken',
            field=models.CharField(max_length=200),
        ),
    ]
