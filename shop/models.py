from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name

class Sneakers(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    last_neme = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "so`m"
    RU = "₽"
    ENG = "$"
    the_price = (
        (UZ, "so`m"),
        (RU, "₽"),
        (ENG, "$"),
    )
    price_type = models.CharField(max_length=10, choices=the_price, default="so`m")
    price = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.name
    
class Buy(models.Model):
    objects = None
    name = models.CharField(max_length=156)
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Sneakers, on_delete=models.CASCADE, null=True)
    ALL_SIZES = (
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
        ("43", "43"),
        ("44", "44"),
    )
    SIZE = models.CharField(max_length=100, choices=ALL_SIZES)
    ALL_VALUES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    how = models.CharField(max_length=100, choices=ALL_VALUES)
    map = models.TextField()
    email = models.EmailField(blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class recklama(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.title
    
    
    
    
    
    
    
    
    