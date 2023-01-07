from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TradeSheet
from .forms import TradeSheetForm
from django.contrib import messages
from .filters import TradeSheetFilter
from django.contrib.auth.decorators import login_required 


@login_required
def displaysheet(request):
    
    if request.method == "POST":
        form = TradeSheetForm(request.POST or None)
        
        if form.is_valid():           
            form.save()
            messages.success(request, ("Trade Added!s"))
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)

        return redirect('tradesheet')

    else:   
        sheet = TradeSheet.objects.all().values()
        myFilter = TradeSheetFilter(request.GET,queryset=sheet)
        sheet = myFilter.qs
        context = {'sheet':sheet, 'myFilter':myFilter}
        return render(request,'tradesheet.html',context)

@login_required
def editTrade(request,id):
    if request.method == "POST":
        sheet = TradeSheet.objects.get(id=id)
        form = TradeSheetForm(request.POST or None,instance=sheet)
        
        if form.is_valid():                    
            form.save()
            messages.success(request, ("Trade Edited!"))
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)

        return redirect('tradesheet')
    else:
        sheet = TradeSheet.objects.get(id=id)
        return render(request,'edit.html',{'trade':sheet})

@login_required
def deleteTrade(request,id):
    TradeSheet.objects.filter(id=id).delete()
    sheet = TradeSheet.objects.all().values()
    #messages.success(request, ("Trade Deleted!"))
    return redirect('tradesheet')
    #return render(request,'tradesheet.html',{'sheet':sheet}) 