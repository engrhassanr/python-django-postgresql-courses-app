# Generated by Django 5.1.6 on 2025-02-17 11:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_course_instructor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
