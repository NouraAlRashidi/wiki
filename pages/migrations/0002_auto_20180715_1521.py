# Generated by Django 2.0.6 on 2018-07-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_update',
            field=models.DateTimeField(),
        ),
    ]
