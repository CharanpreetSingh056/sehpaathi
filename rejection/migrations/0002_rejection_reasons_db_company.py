# Generated by Django 3.2.3 on 2021-05-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rejection_reasons_db',
            name='company',
            field=models.CharField(default='None', max_length=100),
        ),
    ]