# Generated by Django 3.0.7 on 2020-07-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_auto_20200724_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
