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

    def __str__(self) -> str:
        return self.name


