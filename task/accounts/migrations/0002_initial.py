# Generated by Django 4.2.2 on 2023-06-11 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_direction', to='main_app.direction'),
        ),
        migrations.AddField(
            model_name='profile',
            name='doned_tasks',
            field=models.ManyToManyField(blank=True, related_name='doned_tasks', to='main_app.task'),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.group'),
        ),
    ]
