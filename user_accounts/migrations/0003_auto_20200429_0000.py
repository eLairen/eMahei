# Generated by Django 3.0.5 on 2020-04-28 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_accounts', '0002_auto_20200428_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_accounts',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]