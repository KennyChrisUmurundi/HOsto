# Generated by Django 2.2.1 on 2019-07-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortury', '0002_auto_20190722_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpses',
            name='release_status',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]