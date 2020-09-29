from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    points = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    taster_name = models.CharField(max_length=254, null=True, blank=True)
    taster_twitter_handle = models.CharField(max_length=254, null=True, blank=True)
    designation = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    variety = models.CharField(max_length=254, null=True, blank=True)
    region_1 = models.CharField(max_length=254, null=True, blank=True)
    province = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254, null=True, blank=True)
    winery = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title