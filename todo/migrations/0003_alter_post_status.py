# Generated by Django 4.0.6 on 2022-07-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_is_ready_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
