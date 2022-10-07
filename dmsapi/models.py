from django.db import models

# Create your models here.

PHYSICAL, ELECTRONIC = range(1, 3)
TypeDocument = (
    (PHYSICAL, 'Fisico'),
    (ELECTRONIC, 'Electronico'),
)


class Typification(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)
    type_document = models.IntegerField(choices=TypeDocument, default=PHYSICAL)
    amount = models.PositiveIntegerField()
    typification = models.ForeignKey(Typification, blank=False, null=False,
                                     on_delete=models.CASCADE,
                                     related_name='typification',
                                     default=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
