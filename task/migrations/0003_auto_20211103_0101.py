# Generated by Django 3.2.8 on 2021-11-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_taskmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='taskmember',
            name='updated_at',
            field=models.DateTimeField(default=None),
        ),
    ]
