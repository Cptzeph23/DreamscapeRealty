# Generated by Django 4.2 on 2024-12-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0009_rename_name_newuser_fname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textarea', models.TextField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='newuser',
            old_name='fname',
            new_name='name',
        ),
    ]