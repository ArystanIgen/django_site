# Generated by Django 3.1.3 on 2020-12-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cooment_text',
            field=models.TextField(max_length=200, verbose_name='Comment'),
        ),
    ]