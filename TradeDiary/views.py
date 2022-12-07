from django.http import HttpResponse
from django.shortcuts import render
from TradeSheet.models import *
from django.db.models import *


def home(request):
    sheet=TradeSheet.objects.all().values()
    analysis_data={}
    analysis_data.update( sheet.aggregate(Sum('buy_price')))
    analysis_data.update(sheet.aggregate(Sum('profit_loss')))
    total_trades = sheet.count()
    c = TradeSheet.objects.filter(profit_loss__gt=0).count()
    analysis_data['win_rate']=100*c//total_trades
    return render(request,'home.html',analysis_data)

def about(request):
    return render(request,'about.html')
