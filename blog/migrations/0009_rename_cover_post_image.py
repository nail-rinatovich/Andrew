# Generated by Django 5.0.4 on 2024-05-12 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cover',
            new_name='image',
        ),
    ]
