from django.contrib.auth.models import User
from django.db import models


class Avatar(models.Model):
    """
    Модель для хранения аватара пользователя
    """

    src = models.ImageField(
        upload_to="avatars/user_avatars/",
        default="avatars/default.jpg",
        verbose_name="Ссылка",
    )
    alt = models.CharField(max_length=128, verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Аватар"
        verbose_name_plural = "Аватары"


class Profile(models.Model):
    '''
    Модель профиля пользователя
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fullName = models.CharField(max_length=128, verbose_name="Полное имя")
    email = models.EmailField(max_length=80, default='')
    phone = models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name="Номер телефона")
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name="Баланс")
    avatar = models.ForeignKey(
        Avatar,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Аватар",
        null=True,
        blank=True,
)
