# Generated by Django 4.2 on 2024-12-12 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0010_rating_rename_fname_newuser_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='name',
            new_name='fname',
        ),
    ]
