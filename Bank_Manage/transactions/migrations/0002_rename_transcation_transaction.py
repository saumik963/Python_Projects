# Generated by Django 4.2.3 on 2023-08-22 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transcation',
            new_name='Transaction',
        ),
    ]