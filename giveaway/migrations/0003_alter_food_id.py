# Generated by Django 3.2.5 on 2022-02-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0002_alter_food_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
