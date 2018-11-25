# Generated by Django 2.1 on 2018-11-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20181125_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('O', 'Ordered'), ('P', 'Packed'), ('D', 'Delivered'), ('C', 'Cart')], default='C', max_length=2),
        ),
    ]
