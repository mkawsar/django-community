# Generated by Django 2.1.4 on 2019-03-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_group_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
