# Generated by Django 5.0.3 on 2024-07-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_user_about_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='تلفن همراه'),
        ),
    ]
