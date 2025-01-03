# Generated by Django 5.1.4 on 2024-12-31 03:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpgstoneuk', '0003_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='alt_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(upload_to='logos/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'svg', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='logo',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
