# Generated by Django 2.1 on 2018-11-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181122_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('O', 'Ordered'), ('P', 'Packed'), ('D', 'Delivered')], default=0, max_length=2),
        ),
    ]