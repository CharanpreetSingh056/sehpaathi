# Generated by Django 3.2.3 on 2021-05-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interview_experiences_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('interview_experience', models.TextField(max_length=10000)),
                ('company', models.CharField(max_length=100)),
                ('grad_year', models.IntegerField()),
                ('course', models.CharField(max_length=100)),
                ('date_of_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
