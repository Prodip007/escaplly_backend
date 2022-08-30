# Generated by Django 4.1 on 2022-08-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'accessibilities',
            },
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='accessibility',
            field=models.ManyToManyField(blank=True, to='company.accessibility'),
        ),
    ]