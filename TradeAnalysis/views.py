from django.shortcuts import render
from TradeSheet.models import TradeSheet
from django.http import HttpResponse
import plotly.express as px
import pandas as pd
from .graphs import *
from django.db.models import *
import datetime
from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required
def tradeAnalysis(request):
    sheet=TradeSheet.objects.all().values()

    ## Graphs 
    df = pd.DataFrame(sheet)
    Analysis_data = {'pie_chart':pie_chart(df),'line_chart':line_chart(df),'win_by_day':chart_win_by_day(df),'win_by_trade':chart_win_by_trade(df)}

    
    Analysis_data['total_invetment']=df['buy_price'].sum()
    Analysis_data['net_profit']=df['profit_loss'].sum()
    profit_count=df.loc[df['profit_loss']>0,'profit_loss'].count()
    Analysis_data['win_rate']=profit_count*100//len(df)

    today=str(datetime.date.today())
    test=df.groupby(['date'],as_index=False)['profit_loss'].sum()
    test['date']=pd.to_datetime(test['date'])
    todays_pnl = test.loc[test['date']==today]

    if todays_pnl.empty:
        Analysis_data['todays_pnl']=0
    else:
        #print(toda)
        Analysis_data['todays_pnl']=todays_pnl.iloc[0]['profit_loss']

    return render(request,'analysis.html',Analysis_data)

