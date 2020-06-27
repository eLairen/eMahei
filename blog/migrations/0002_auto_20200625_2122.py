# Generated by Django 3.0.5 on 2020-06-25 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Blog Category',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='about_author',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='author_picture',
            field=models.FileField(null=True, upload_to='author_pic/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog_category'),
        ),
    ]
