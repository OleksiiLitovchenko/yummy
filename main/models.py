from django.db import models
from django.core.validators import RegexValidator
from pyexpat.errors import messages


class DishCategory(models.Model):
    name = models.CharField(max_length=100)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,max_length=50,db_index=True)


    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


class Dish(models.Model):
    name = models.CharField(max_length=100)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=500)
    ingredients = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="images/", blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name="dishes")
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Gallary(models.Model):
    photo = models.ImageField(upload_to="gallery/")
    is_visible = models.BooleanField(default=True)



class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^[0-9]{9}$',
        message='Phone number must be entered in the format: 999999999'
    )

    phone = models.CharField(validators=[phone_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=500, blank=True)

    is_processed = models.BooleanField(default=False)
    date_in= models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date} - {self.phone}: {self.date}, {self.time}'

    class Meta:
        ordering = ['-date']


class Chef(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="chef/")
    is_visible = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="events/")
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name