# Generated by Django 3.0.4 on 2020-04-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tsite', '0008_auto_20200413_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerskey',
            name='lvl_4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
