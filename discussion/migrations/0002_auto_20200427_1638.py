# Generated by Django 3.0.5 on 2020-04-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='topic',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discussion',
            name='discussion_text',
            field=models.TextField(max_length=500),
        ),
    ]