# Generated by Django 2.2.1 on 2019-05-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190529_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]