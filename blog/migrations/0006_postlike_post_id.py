# Generated by Django 2.1.4 on 2019-03-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190307_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='post_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
