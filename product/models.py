from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.category}'


STARS = [(i, '*' * i) for i in range(1, 11)]


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="reviews")
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=STARS, default=1)

    def __str__(self):
        return f'{self.stars} - {self.text}'
