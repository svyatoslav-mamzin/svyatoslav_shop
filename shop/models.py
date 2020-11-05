from django.db import models
from django.urls import reverse


class Product(models.Model):

    article = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
