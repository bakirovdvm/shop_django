# Generated by Django 5.0.4 on 2024-04-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productimage_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
