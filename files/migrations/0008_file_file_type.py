# Generated by Django 3.2.7 on 2021-09-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_file_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]