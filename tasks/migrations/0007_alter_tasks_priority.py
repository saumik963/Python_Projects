# Generated by Django 4.2.6 on 2023-10-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_tasks_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='Priority',
            field=models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], max_length=30),
        ),
    ]
