# Generated by Django 5.2 on 2025-04-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_info_color_alter_info_mileage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('diameter', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
