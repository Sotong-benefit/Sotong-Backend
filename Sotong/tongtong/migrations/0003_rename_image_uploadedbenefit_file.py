# Generated by Django 4.2.4 on 2023-08-12 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tongtong', '0002_uploadedbenefit_delete_uploadedimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedbenefit',
            old_name='image',
            new_name='file',
        ),
    ]
