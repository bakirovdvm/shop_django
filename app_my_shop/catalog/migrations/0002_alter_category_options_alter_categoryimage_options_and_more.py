# Generated by Django 5.0.4 on 2024-04-24 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='categoryimage',
            options={'verbose_name': 'Картинка категории', 'verbose_name_plural': 'Картинки категорий'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Под-категория', 'verbose_name_plural': 'Под-категории'},
        ),
        migrations.AlterModelOptions(
            name='subcategoryimage',
            options={'verbose_name': 'Картинка под-категории', 'verbose_name_plural': 'Картинки под-категорий'},
        ),
        migrations.RenameField(
            model_name='subcategoryimage',
            old_name='category',
            new_name='subcategory',
        ),
    ]