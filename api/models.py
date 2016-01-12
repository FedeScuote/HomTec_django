from django.core.validators import RegexValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

STATE_CHOICES = (
    ('MVD', 'Montevideo'),
    ('ART', 'Artigas'),
    ('CAN', 'Canelones'),
    ('CER', 'Cerro Largo'),
    ('COL', 'Colonia'),
    ('DUR', 'Durazno'),
    ('FLO', 'Flores'),
    ('FLA', 'Florida'),
    ('LAV', 'Lavalleja'),
    ('MAL', 'Maldonado'),
    ('PAY', 'Paysandu'),
    ('RNG', 'Rio Negro'),
    ('RIV', 'Rivera'),
    ('RCH', 'Rocha'),
    ('SAL', 'Salto'),
    ('SAJ', 'San Jose'),
    ('SOR', 'Soriano'),
    ('TAC', 'Tacuarembo'),
    ('TYT', 'Treinta y Tres'),
)

# Reg expression for phone validation
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


# The one who will use the mobile app.
class MobileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default='MVD')
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)


# The Technician who will pay to appear on the app
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Boolean to check if the Client is active
    active = models.BooleanField(default=True)
    rut = models.IntegerField(verbose_name="RUT", validators=[MaxValueValidator])
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default='MVD')
    country = CountryField()
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    logo = models.ImageField()
    category = models.CharField(max_length=20, )
    description = models.TextField()


class Publication (models.Model):
    client = models.ForeignKey('Client')


































