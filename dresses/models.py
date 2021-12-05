from django.db import models

# Create your models here.



class kurta(models.Model):
    image=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    price=models.FloatField()
    color=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    neck=models.CharField(max_length=100)
    sleeve=models.CharField(max_length=100)
    material=models.CharField(max_length=100)


class kurtaset(models.Model):
    image=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    price=models.FloatField()
    color=models.CharField(max_length=500)
    type=models.CharField(max_length=500)
    neck=models.CharField(max_length=100)
    sleeve=models.CharField(max_length=100)
    material=models.CharField(max_length=500)


class saree(models.Model):
    image=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=3000)
    price=models.FloatField()
    color=models.CharField(max_length=500)
    material=models.CharField(max_length=500)


class top(models.Model):
    image=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    price=models.FloatField()
    color=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    neck=models.CharField(max_length=100)
    sleeve=models.CharField(max_length=100)
    material=models.CharField(max_length=100)


class jewellery(models.Model):
    image=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    price=models.FloatField()


class handbag(models.Model):
    image = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    height=models.FloatField()
    width=models.FloatField()


