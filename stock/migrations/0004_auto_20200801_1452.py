# Generated by Django 3.0.8 on 2020-08-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20200801_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Manufacturing_Date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='TM_Invoice_Date',
            field=models.CharField(max_length=100),
        ),
    ]