from django.db import models


# 水果模型
class Fruit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12, )
    price = models.IntegerField()
    link = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


# 饮料模型
class Drink(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    link = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


# 零食模型
class Snack(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    link = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


# 日用品模型
class Dayly(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    link = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


# 电子用品模型
class Electron(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    link = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name

