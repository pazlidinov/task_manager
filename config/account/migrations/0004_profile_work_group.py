# Generated by Django 4.2.2 on 2023-06-10 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_group'),
        ('account', '0003_profile_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='work_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.group'),
        ),
    ]