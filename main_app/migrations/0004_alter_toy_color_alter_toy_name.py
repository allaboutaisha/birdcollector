# Generated by Django 4.1.5 on 2023-01-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_alter_feeding_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='color',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='toy',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
