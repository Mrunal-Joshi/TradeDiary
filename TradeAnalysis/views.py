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
    # sheet=TradeSheet.objects.all().values()
    current_user=request.user   
    sheet = TradeSheet.objects.filter(user=current_user).values()
    ## Graphs 
    df = pd.DataFrame(sheet)
    if df.empty:
        Analysis_data = {'pie_chart':" ",'line_chart':" ",'win_by_day':" ",'win_by_trade':" ",'total_invetment':0,'net_profit':0,
        'profit_loss':0,'win_rate':0,'total_profit':0,'total_loss':0,'todays_pnl':0 ,'profit_loss_per_share':None} 

        return render(request,'analysis.html',Analysis_data)
    else:
        Analysis_data = {'pie_chart':pie_chart(df),'line_chart':line_chart(df),'win_by_day':chart_win_by_day(df),
        'win_by_trade':chart_win_by_trade(df), 'profit_loss_per_share':chart_profit_loss_per_share(df)}

        
        Analysis_data['total_invetment']=df['buy_price'].sum()
        Analysis_data['net_profit']=df['profit_loss'].sum()
        profit_count=df.loc[df['profit_loss']>0,'profit_loss'].count()
        Analysis_data['win_rate']=profit_count*100//len(df)

        Analysis_data['total_profit']=df.loc[df['profit_loss']>0,'profit_loss'].sum()
        Analysis_data['total_loss']=df.loc[df['profit_loss']<0,'profit_loss'].sum()


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

