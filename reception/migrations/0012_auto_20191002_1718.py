# Generated by Django 2.2.1 on 2019-10-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0011_auto_20190731_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.CharField(default='no', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(default='O+', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='diabetic',
            field=models.CharField(default='no', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_identification',
            field=models.CharField(default='123456789', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.CharField(default='75', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.FileField(upload_to='profile_pics'),
        ),
    ]
