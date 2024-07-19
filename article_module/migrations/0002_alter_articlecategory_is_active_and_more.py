# Generated by Django 5.0.3 on 2024-07-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان دسته بندی'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='url_title',
            field=models.CharField(max_length=200, verbose_name='عنوان در url'),
        ),
    ]