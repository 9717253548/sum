# Generated by Django 3.0.8 on 2020-08-02 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20200801_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AlterField(
            model_name='stock',
            name='Chassis_No',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]