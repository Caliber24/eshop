# Generated by Django 5.0.3 on 2024-07-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemodule', '0008_slider_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر'),
        ),
    ]
