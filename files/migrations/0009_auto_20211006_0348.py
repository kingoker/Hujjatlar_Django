# Generated by Django 3.2.7 on 2021-10-06 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0008_file_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directory_objects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_objects', to=settings.AUTH_USER_MODEL),
        ),
    ]
