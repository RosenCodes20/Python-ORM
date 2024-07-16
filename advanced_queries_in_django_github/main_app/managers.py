from django.db import models


class ProductManager(models.Manager):

    def available_products(self):
        return self.filter(is_available=True)

    def available_products_in_category(self, category_name):
        return self.filter(is_available=True, category__name=category_name)