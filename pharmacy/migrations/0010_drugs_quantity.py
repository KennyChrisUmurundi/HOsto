# Generated by Django 2.2.1 on 2019-08-05 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0009_auto_20190805_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='quantity',
            field=models.CharField(default=5),
            preserve_default=False,
        ),
    ]
