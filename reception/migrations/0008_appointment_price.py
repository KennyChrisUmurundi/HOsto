# Generated by Django 2.2.1 on 2019-07-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0007_delete_teststatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
