# Generated by Django 5.1.5 on 2025-04-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_alter_image_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateField(auto_now_add=True, default='2025-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='updated_at',
            field=models.DateField(auto_now_add=True, default='2025-01-01'),
            preserve_default=False,
        ),
    ]
