# Generated by Django 4.1.3 on 2023-02-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_registermodel_gender_alter_registermodel_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('t_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('t_amt', models.IntegerField()),
                ('preparation', models.CharField(max_length=100, null=True)),
                ('sample', models.CharField(max_length=100)),
                ('test_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
