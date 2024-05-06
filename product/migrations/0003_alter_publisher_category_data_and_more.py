# Generated by Django 4.2.11 on 2024-04-17 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_publisher_category_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='category_data',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='writer',
            name='category_data',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('category_data', models.CharField(blank=True, editable=False, max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('years', models.IntegerField()),
                ('description', models.TextField()),
                ('cover_book', models.CharField(blank=True, max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('avail_stock', models.IntegerField(default=0)),
                ('isbn', models.CharField(blank=True, max_length=255)),
                ('weight', models.FloatField(default=0.0)),
                ('width', models.FloatField(default=0.0)),
                ('length', models.FloatField(default=0.0)),
                ('pages_count', models.IntegerField(default=0)),
                ('is_discount', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0)),
                ('price_discount', models.IntegerField(default=0)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.publisher')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.writer')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]