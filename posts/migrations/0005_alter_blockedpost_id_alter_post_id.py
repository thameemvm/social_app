# Generated by Django 4.2.11 on 2024-05-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_blockedpost_blocked_whom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
