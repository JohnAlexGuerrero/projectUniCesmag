# Generated by Django 5.1.5 on 2025-02-05 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_alter_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='titulo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='imagen')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
