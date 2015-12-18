from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


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


# The one who will use the mobile app.
class MobileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, default='MVD')

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True)  # validators should be a list
