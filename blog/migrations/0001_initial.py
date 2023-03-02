# Generated by Django 3.2.18 on 2023-03-02 18:03

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'موضوع',
                'verbose_name_plural': 'موضوعات',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='اسلاگ')),
                ('title', models.CharField(max_length=100, verbose_name='موضوع')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('last_update', models.DateTimeField(null=True, verbose_name='اخرین بروز رسانی')),
                ('img', models.ImageField(null=True, upload_to=blog.models.user_directory_path, verbose_name='عکس')),
                ('body', models.TextField(verbose_name='بدنه')),
                ('show', models.BooleanField(default=True, verbose_name='نمایش')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.author', verbose_name='نویسنده')),
                ('categories', models.ManyToManyField(to='blog.Category', verbose_name='موضوعات')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پستها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='متن ')),
                ('rating', models.IntegerField(choices=[(1, 'Low'), (2, 'NotRecommended'), (3, 'Normal'), (4, 'Recommended'), (5, 'HighlyRecommended')], default=None, null=True, verbose_name='امتیاز')),
                ('show', models.BooleanField(default=True, verbose_name='نمایش')),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ انتشار')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.post', verbose_name='پست مربوطه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
            },
        ),
    ]
