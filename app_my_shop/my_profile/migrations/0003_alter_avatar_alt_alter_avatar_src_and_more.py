# Generated by Django 5.0.4 on 2024-04-12 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_profile_email_alter_avatar_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='alt',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='src',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars/user_avatars/', verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='my_profile.avatar', verbose_name='Аватар'),
        ),
    ]