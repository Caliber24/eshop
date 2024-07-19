# Generated by Django 5.0.3 on 2024-07-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_alter_articlecategory_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name': 'دسته بندی مقاله', 'verbose_name_plural': 'دسته بندی های مقاله'},
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='url_title',
            field=models.CharField(max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
    ]