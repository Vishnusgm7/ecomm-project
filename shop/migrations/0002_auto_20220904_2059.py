# Generated by Django 2.2 on 2022-09-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categ',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categ',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]