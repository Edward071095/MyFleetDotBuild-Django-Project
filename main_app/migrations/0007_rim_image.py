# Generated by Django 5.2 on 2025-04-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rim'),
    ]

    operations = [
        migrations.AddField(
            model_name='rim',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rim_images/'),
        ),
    ]
