# Generated by Django 5.0.4 on 2024-05-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0002_alter_contact_is_read_by_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]