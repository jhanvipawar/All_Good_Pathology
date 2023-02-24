# Generated by Django 4.1.3 on 2023-02-24 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0047_alter_patientlist_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientlist',
            name='id',
        ),
        migrations.AlterField(
            model_name='patientlist',
            name='p_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patientlist',
            name='username',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', unique=True),
        ),
        migrations.AlterModelTable(
            name='patientlist',
            table='PatientList',
        ),
    ]