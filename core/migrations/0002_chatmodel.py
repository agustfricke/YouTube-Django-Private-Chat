# Generated by Django 4.1.5 on 2023-01-04 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default=None, max_length=50)),
                ('message', models.CharField(blank=True, max_length=50)),
                ('thread_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
