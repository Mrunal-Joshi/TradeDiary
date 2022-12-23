import django_filters
from django import forms
from .models import *
from django_filters import CharFilter
from django_filters import DateFilter
from django_filters import NumberFilter

class TradeSheetFilter(django_filters.FilterSet):
    Symbol = CharFilter(field_name = "symbol",widget=forms.TextInput(attrs={"class":"form-control m-1","size":"10"}))
    Date = DateFilter(field_name = "date",widget=forms.DateInput(attrs={"class":"form-control m-1","size":"10",'type': 'date'}))
    BuyPrice = CharFilter(field_name = "buy_price",widget=forms.TextInput(attrs={"class":"form-control m-1","size":"10"}))
    SellPrice = CharFilter(field_name = "sell_price",widget=forms.TextInput(attrs={"class":"form-control m-1","max_length" : "20","size":"10"}))
    class Meta:
        model = TradeSheet
        fields = '__all__'
        exclude = ['no_of_shares','profit_loss','symbol','date','buy_price','sell_price','notes']
