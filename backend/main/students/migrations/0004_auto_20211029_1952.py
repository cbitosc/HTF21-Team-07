# Generated by Django 3.2.8 on 2021-10-29 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20210305_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenttaskimage',
            name='student_task',
        ),
        migrations.DeleteModel(
            name='StudentTask',
        ),
        migrations.DeleteModel(
            name='StudentTaskImage',
        ),
    ]
