from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Product(models.Model):


    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    product_img = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
