# Generated by Django 5.0.6 on 2024-09-03 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omsanatanaapp', '0002_alter_book_options_remove_book_pdf_location_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.AlterModelOptions(
            name='bookpdf',
            options={},
        ),
        migrations.AlterModelTable(
            name='book',
            table='news',
        ),
        migrations.AlterModelTable(
            name='bookpdf',
            table=None,
        ),
    ]
