# Generated by Django 3.2.3 on 2021-05-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]