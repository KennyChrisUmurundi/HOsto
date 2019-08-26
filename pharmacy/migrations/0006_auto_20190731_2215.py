# Generated by Django 2.2.1 on 2019-07-31 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_auto_20190703_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='effects',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drugs',
            name='expire_date',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drugs',
            name='purchasedPrice',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drugs',
            name='supplier',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]