from django.contrib.auth.models import User
from django.db import models


STATUS_SESSION = [
    (1, 'Активно'),
    (2, 'Неактивно'),
    (3, 'На паузе')
]
# class StatusSession(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name


class Session(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    teamCount = models.PositiveSmallIntegerField(verbose_name="Кол-во команд")
    link = models.CharField(max_length=255, verbose_name="Ссылка")
    password = models.CharField(max_length=255, verbose_name="Пароль")
    datetimeStart = models.DateTimeField(auto_now_add=True, verbose_name="Начало")
    status = models.PositiveSmallIntegerField(choices=STATUS_SESSION, verbose_name="Статус", default=1)
    timer = models.TimeField(verbose_name="Таймер")
    timerIsActive = models.BooleanField(verbose_name="Активность таймера")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    pincode = models.PositiveSmallIntegerField(verbose_name="Пин-код")
    userCount = models.PositiveSmallIntegerField(verbose_name="Кол-во игроков")
    sessionID = models.ForeignKey(Session, on_delete=models.PROTECT, related_name='team', verbose_name="Игра")
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
