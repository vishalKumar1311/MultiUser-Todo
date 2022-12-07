# Generated by Django 4.0.3 on 2022-11-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('C', 'Completed'), ('P', 'Pending')], max_length=2)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
