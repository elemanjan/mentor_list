# Generated by Django 3.1.6 on 2021-03-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
