# Generated by Django 2.2.1 on 2019-07-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortury', '0003_corpses_release_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpses',
            name='release_status',
            field=models.CharField(default='Not Approved', max_length=500),
        ),
    ]