# Generated by Django 2.2.1 on 2019-08-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0010_drugs_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='quantity',
            field=models.CharField(max_length=300),
        ),
    ]
