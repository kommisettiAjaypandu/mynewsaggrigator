# Generated by Django 2.2.6 on 2019-12-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
