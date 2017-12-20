from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=128, db_index=True,
    )
    description = models.TextField()
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    category = models.ForeignKey(
        'products.Category',
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=128, db_index=True,
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
