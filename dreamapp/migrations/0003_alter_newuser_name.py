# Generated by Django 4.1 on 2024-12-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]