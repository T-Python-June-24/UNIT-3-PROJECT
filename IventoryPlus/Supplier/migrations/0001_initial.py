# Generated by Django 5.0.7 on 2024-07-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('phone_number', models.CharField(max_length=12)),
                ('website', models.URLField()),
            ],
        ),
    ]
