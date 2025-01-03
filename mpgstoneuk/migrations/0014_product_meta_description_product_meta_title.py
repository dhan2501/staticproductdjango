# Generated by Django 5.1.4 on 2025-01-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpgstoneuk', '0013_pagestitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, help_text='SEO meta description', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, help_text='SEO meta title', max_length=255, null=True),
        ),
    ]