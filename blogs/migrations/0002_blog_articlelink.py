# Generated by Django 4.1.5 on 2023-04-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='articleLink',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]
