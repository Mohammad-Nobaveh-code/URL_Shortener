# Generated by Django 4.1 on 2022-08-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shorten_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
