# Generated by Django 4.0.1 on 2022-09-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QT', '0002_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(max_length=20)),
                ('Dev_Name', models.CharField(max_length=20)),
                ('Project_Report', models.CharField(max_length=2000)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
    ]
