# Generated by Django 4.2.3 on 2023-07-27 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_advertising'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertising',
            old_name='image',
            new_name='Image',
        ),
    ]
