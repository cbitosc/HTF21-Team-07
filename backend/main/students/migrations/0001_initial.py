# Generated by Django 3.1.5 on 2021-01-22 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admins', '0002_studentattend_taskreport_taskreportstudent_tasksession'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('got_marks', models.IntegerField(blank=True, null=True)),
                ('feedback', models.CharField(blank=True, max_length=255, null=True)),
                ('is_corrected', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_task', to='admins.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentTaskImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='students_tasks_images/')),
                ('student_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_task_image', to='students.studenttask')),
            ],
        ),
    ]
