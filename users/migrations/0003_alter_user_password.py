# Generated by Django 4.0.4 on 2022-05-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Пароль'),
        ),
    ]
