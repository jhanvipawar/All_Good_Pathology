# Generated by Django 4.1.3 on 2023-02-24 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_remove_doctor_d_name_delete_docfullname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientlist',
            old_name='username',
            new_name='userchanav',
        ),
    ]
