# Generated by Django 5.0.3 on 2024-07-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemodule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='address',
            field=models.CharField(max_length=200, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='fax',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن'),
        ),
    ]
