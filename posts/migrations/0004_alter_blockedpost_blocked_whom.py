# Generated by Django 4.2.11 on 2024-05-01 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20180404_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedpost',
            name='blocked_whom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocked_whom', to=settings.AUTH_USER_MODEL),
        ),
    ]