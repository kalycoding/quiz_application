# Generated by Django 3.1.4 on 2020-12-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0026_auto_20201227_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='scores',
            field=models.FloatField(default=0),
        ),
    ]
