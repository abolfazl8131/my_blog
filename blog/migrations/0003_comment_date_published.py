# Generated by Django 3.2.18 on 2023-02-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
