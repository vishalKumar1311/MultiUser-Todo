# Generated by Django 4.0.3 on 2022-12-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('✅', 'Completed'), ('⏳', 'Pending')], max_length=2),
        ),
    ]
