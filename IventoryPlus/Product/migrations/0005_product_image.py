# Generated by Django 5.0.7 on 2024-07-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_remove_product_last_stock_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
