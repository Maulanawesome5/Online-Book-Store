# Generated by Django 4.2.11 on 2024-04-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('category_data', models.CharField(choices=[('writer', 'Book Writer'), ('publisher', 'Book Publisher'), ('book', 'Book')], max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('about', models.TextField(blank=True, null=True)),
                ('images', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('category_data', models.CharField(choices=[('writer', 'Book Writer'), ('publisher', 'Book Publisher'), ('book', 'Book')], max_length=50)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('images', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
