# Generated by Django 4.1.3 on 2023-02-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0068_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('radio_selection', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
