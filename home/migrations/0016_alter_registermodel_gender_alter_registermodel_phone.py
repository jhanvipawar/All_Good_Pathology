# Generated by Django 4.1.3 on 2023-01-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_registermodel_repassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
