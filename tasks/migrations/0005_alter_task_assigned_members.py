# Generated by Django 4.0.6 on 2022-08-07 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_email_profile_name_profile_username_and_more'),
        ('tasks', '0004_task_assigned_members_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_members',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_members', to='users.profile'),
        ),
    ]