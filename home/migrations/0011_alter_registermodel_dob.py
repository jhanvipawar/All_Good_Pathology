# Generated by Django 4.1.3 on 2022-11-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_registermodel_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='dob',
            field=models.DateField(),
        ),
    ]
