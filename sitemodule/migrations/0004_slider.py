# Generated by Django 5.0.3 on 2024-07-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemodule', '0003_footerlinkbox_footerlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات اسلایدر')),
                ('url', models.TextField(verbose_name='ادرس')),
                ('url_title', models.TextField(verbose_name='عنوان لینک')),
                ('image', models.ImageField(upload_to='image/sliders', verbose_name='تصویر اسلایدر')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]
