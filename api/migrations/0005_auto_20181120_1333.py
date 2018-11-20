# Generated by Django 2.1 on 2018-11-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181120_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='appartment',
            field=models.CharField(default='1', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='floor',
            field=models.PositiveIntegerField(),
        ),
    ]