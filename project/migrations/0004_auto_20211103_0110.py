# Generated by Django 3.2.8 on 2021-11-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20211103_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='projectcolumn',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
