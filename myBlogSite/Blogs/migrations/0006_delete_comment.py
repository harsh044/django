# Generated by Django 3.2.4 on 2021-06-12 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0005_post_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
