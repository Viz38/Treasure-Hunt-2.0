# Generated by Django 3.0.4 on 2020-04-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tsite', '0007_auto_20200405_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='l1_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='l2_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='l3_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='l4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='l4_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='l5_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
