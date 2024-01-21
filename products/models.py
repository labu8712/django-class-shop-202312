from django.db import models


class Category(models.Model):
    class Status(models.IntegerChoices):
        HIDE = 0
        SHOW = 1

    name = models.CharField(max_length=255, unique=True)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.SHOW,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Status(models.IntegerChoices):
        HIDE = 0
        SHOW = 1

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.SHOW,
    )

    count = models.PositiveBigIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
