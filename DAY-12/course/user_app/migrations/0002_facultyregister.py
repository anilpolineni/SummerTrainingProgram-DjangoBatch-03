# Generated by Django 3.0.7 on 2020-07-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('dob', models.DateField(null=True)),
            ],
        ),
    ]