# Generated by Django 2.2.1 on 2019-07-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortury', '0005_auto_20190723_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morturypayment',
            name='status',
            field=models.CharField(default='Not Paid', max_length=300),
        ),
    ]