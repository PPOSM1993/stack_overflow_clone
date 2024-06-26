# Generated by Django 5.0.6 on 2024-06-12 15:37

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='stackoverflow.question')),
            ],
        ),
    ]
