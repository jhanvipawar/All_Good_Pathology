# Generated by Django 4.1.3 on 2023-03-07 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0088_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='b_id',
        ),
    ]