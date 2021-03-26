from django.db import models


class DefaultModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Client(DefaultModel):
    CLIENT_CATEGORY_CHOICES = [
        ('eventual', 'Eventual'),
        ('frequent', 'Frequente'),
        ('premium', 'Premium')
    ]
    name = models.CharField(max_length=100)
    cpf = models.IntegerField(max_length=11, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CLIENT_CATEGORY_CHOICES, default='eventual')


class Car(DefaultModel):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    brand_model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=15, blank=True, null=True)
    color_code = models.CharField(max_length=30, blank=True, null=True)
