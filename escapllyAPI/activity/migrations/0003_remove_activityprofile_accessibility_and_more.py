# Generated by Django 4.1 on 2022-08-30 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_alter_accessibility_options_alter_activity_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityprofile',
            name='accessibility',
        ),
        migrations.DeleteModel(
            name='Accessibility',
        ),
    ]