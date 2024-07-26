# Generated by Django 5.0.7 on 2024-07-25 14:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
        ('Supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('expiry_date', models.DateField()),
                ('stock', models.IntegerField(default=0)),
                ('minimum_stock', models.IntegerField(default=0)),
                ('last_stock_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Category.category')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Supplier.supplier')),
            ],
        ),
    ]
