# Generated by Django 2.2 on 2022-09-05 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20220905_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartlist',
            old_name='card_id',
            new_name='cart_id',
        ),
    ]
