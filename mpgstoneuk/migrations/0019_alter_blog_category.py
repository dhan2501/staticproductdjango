# Generated by Django 5.1.4 on 2025-01-03 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpgstoneuk', '0018_blog_content_blog_meta_description_blog_meta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='mpgstoneuk.blogcategory'),
        ),
    ]