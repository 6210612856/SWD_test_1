# Generated by Django 5.0.2 on 2024-02-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('desc', models.CharField(max_length=1000)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]