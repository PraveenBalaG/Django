# Generated by Django 4.0.1 on 2022-09-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QT', '0003_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(max_length=20)),
                ('Work_To_Do', models.CharField(max_length=200)),
            ],
        ),
    ]
