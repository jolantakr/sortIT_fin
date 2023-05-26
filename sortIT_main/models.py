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


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
