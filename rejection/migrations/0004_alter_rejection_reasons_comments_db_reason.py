# Generated by Django 3.2.3 on 2021-05-28 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rejection', '0003_rename_question_rejection_reasons_db_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rejection_reasons_comments_db',
            name='reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='rejection.rejection_reasons_db'),
        ),
    ]
