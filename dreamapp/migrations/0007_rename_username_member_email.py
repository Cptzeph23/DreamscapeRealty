# Generated by Django 4.1 on 2024-12-05 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0006_remove_newuser_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='username',
            new_name='email',
        ),
    ]