from django.db import models

# Create your models here.
class sprice(models.Model):
    stockName = models.CharField(max_length = 50)
    stockType = models.CharField(max_length = 50)
    exchangeName = models.CharField(max_length = 50)
    stockPrice = models.IntegerField()
    market = models.ForeignKey('market', on_delete=models.SET_NULL, null=True)
    class Meta:
	    db_table = "stock_price"
class market(models.Model):
  name = models.CharField(max_length = 50) 
  city = models.CharField(max_length = 50) 
  class Meta: 
    db_table = "market"
        
    

