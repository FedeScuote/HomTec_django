from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
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


# Category that will fit to a publication
class Category (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


# Subcategory for a more descriptive value, that will fit into a category
class SubCategory(models.Model):
    category = models.ForeignKey('Category', null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "sub categories"


# The one who will use the mobile app.
class MobileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default='MVD')
    country = CountryField(default='UY')
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.user.name


# The Technician who will pay to appear on the app
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Boolean to check if the Client is active
    active = models.BooleanField(default=True)
    rut = models.IntegerField(verbose_name="RUT", validators=[MaxValueValidator])
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default='MVD')
    country = CountryField(default='UY')
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    logo = models.ImageField()
    category = models.ForeignKey('Category')
    description = models.TextField()

    def __str__(self):
        return self.user.name


# When a User does a publication, until it gets completed
class Publication (models.Model):
    client = models.ForeignKey('Client', null=True)
    mobile_user = models.ForeignKey('MobileUser')
    completed = models.BooleanField(default=False)
    description = models.TextField(null=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.client.user.name + ' ' + self.mobile_user.user.name


# Rating that is given to a Client
class Rating (models.Model):
    stars = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    comment = models.TextField()
    user = models.ForeignKey('Client', null=True)

    def __str__(self):
        return self.user.name + ' ' + self.stars
