# Generated by Django 2.1.2 on 2018-10-24 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20181024_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
