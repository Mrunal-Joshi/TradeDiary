from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class TradeSheet(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tradesheet", null=True)
    date = models.DateField(auto_now=False, auto_now_add=False,blank=True,default=datetime.now)
    symbol = models.CharField(max_length=8)
    no_of_shares = models.IntegerField(default=0)
    buy_price = models.FloatField(default=0)
    sell_price = models.FloatField(default=0)
    profit_loss = models.FloatField(default=0)
    notes = models.TextField(default="")

    class Meta:
        verbose_name = ("Trading Sheet")
        ordering = ("-date",)
    

    def __str__(self):
        """Every element will be stored as object , Therefore returning the name you want to display"""
        return self.symbol

    def get_absolute_url(self):      
        return reverse("_detail", kwargs={"pk": self.pk})

    def save(self,*args,**kwargs):
        self.profit_loss = (self.sell_price-self.buy_price)*self.no_of_shares
        super(TradeSheet,self).save(*args,**kwargs)

