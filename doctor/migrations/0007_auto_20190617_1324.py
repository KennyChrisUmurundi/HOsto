# Generated by Django 2.2.1 on 2019-06-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_reports_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='reports',
            name='report',
            field=models.TextField(),
        ),
    ]
