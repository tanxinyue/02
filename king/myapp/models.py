from django.db import models

# Create your models here.



class GOODS(models.Model):
    name=models.CharField(max_length=30,verbose_name='商品名称')
    price=models.CharField(max_length=128,verbose_name='商品价格')
    num=models.CharField(max_length=128,verbose_name='商品数量')



