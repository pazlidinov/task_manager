# Generated by Django 4.2.2 on 2023-06-10 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('link', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='task_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main_app.group')),
            ],
        ),
    ]