"""Module that keep and describe all project models."""
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    """Model that describes flat."""
    BUILDING_CHOICES = ((True, 'Да'), (False, 'Нет'), (None, 'Неизвестно'))

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True,
    )
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True,
    )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное',
    )
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4',
    )
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж',
    )

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True,
    )
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True,
    )

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True,
    )
    is_building_new = models.BooleanField(
        'Новостройка', choices=BUILDING_CHOICES, null=True, default=None, db_index=True,
    )
    liked_by = models.ManyToManyField(
        User, related_name='liked_flats', blank=True, verbose_name='Кто поставил лайк', db_index=True,
    )

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    """Model that describes complaint."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто жаловался', related_name='complaints')
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name='Квартира, на которую пожаловались',
        related_name='complaints',
    )
    text = models.TextField(verbose_name='Текст жалобы')

    class Meta:
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"

    def __str__(self):
        return f'Жалоба на квартиру {self.flat.address}'


class Owner(models.Model):
    """Model that describes owner of flat(s)."""
    full_name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20, db_index=True)
    owner_normalized_phone = PhoneNumberField(blank=True, verbose_name='Нормализованный номер владельца', db_index=True)
    flats = models.ManyToManyField(Flat, related_name='owners', verbose_name='Квартиры в собственности', db_index=True)

    class Meta:
        verbose_name = "Собственник"
        verbose_name_plural = "Собственники"

    def __str__(self):
        return self.full_name
