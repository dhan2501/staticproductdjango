# Generated by Django 5.1.4 on 2024-12-31 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpgstoneuk', '0007_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
    ]
