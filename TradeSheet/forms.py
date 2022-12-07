from django import forms
from .models import TradeSheet

class TradeSheetForm(forms.ModelForm):
    
    class Meta:
        model = TradeSheet
        fields = ["date","symbol","no_of_shares","buy_price","sell_price","notes"]
        exclude = ["profit_loss"]
