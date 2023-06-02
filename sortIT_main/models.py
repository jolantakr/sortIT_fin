from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    detail1_name = models.CharField(max_length=100)
    detail1_description = models.TextField()
    detail2_name = models.CharField(max_length=100)
    detail2_description = models.TextField()
    detail3_name = models.CharField(max_length=100)
    detail3_description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Categories"


class Containers(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    detail1_name = models.CharField(max_length=100)
    detail1_description = models.TextField()
    detail2_name = models.CharField(max_length=100)
    detail2_description = models.TextField()
    detail3_name = models.CharField(max_length=100)
    detail3_description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Containers"


class Location(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, default=0.0)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, default=0.0)

    def __str__(self):
        return f"{self.name}"
