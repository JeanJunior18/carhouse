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
    cpf = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CLIENT_CATEGORY_CHOICES, default='eventual')

    def __str__(self):
        return self.name


class Car(DefaultModel):
    CAR_CATEGORY_CHOICES = [
        ('popular', 'Carro Popular'),
        ('luxury', 'Carro de Luxo'),
        ('sporting', 'Carro esportivo'),
        ('suv', 'SUV'),
        ('pickup', 'Caminhonete'),
        ('van_minivan', 'Van/MiniVan'),
        ('motorbike', 'Moto Comum'),
        ('sports_bike', 'Moto Esportiva'),
        ('other', 'Outro')
    ]
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    brand_model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=15, blank=True, null=True)
    color_code = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CAR_CATEGORY_CHOICES, default='popular')

    def __str__(self):
        return self.brand_model
