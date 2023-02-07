# Generated by Django 4.1.3 on 2023-02-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_test_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('package_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=13)),
                ('package_amt', models.IntegerField()),
                ('preparation', models.CharField(max_length=200)),
                ('sample', models.CharField(max_length=200)),
                ('package_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
