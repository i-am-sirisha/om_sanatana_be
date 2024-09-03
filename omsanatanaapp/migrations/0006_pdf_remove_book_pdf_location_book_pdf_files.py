# Generated by Django 5.0.6 on 2024-09-03 19:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omsanatanaapp', '0005_alter_book_pdf_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('_id', models.CharField(db_column='_id', default=uuid.uuid1, editable=False, max_length=45, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('file_path', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='pdf_location',
        ),
        migrations.AddField(
            model_name='book',
            name='pdf_files',
            field=models.ManyToManyField(blank=True, to='omsanatanaapp.pdf'),
        ),
    ]
