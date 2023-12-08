from django.shortcuts import render, get_object_or_404,redirect
from .models import StockData

# Create your views here.

def homepage(request):
    stock_data = StockData.objects.all()

    context ={
        'stock_data': stock_data
    }
    return render(request,'homepage.html',context)


def edit_stock_entry(request, entry_id):
    entry = get_object_or_404(StockData, id=entry_id)

    if request.method == 'POST':
        # Handle form submission and update the entry
        entry.date = request.POST.get('date', entry.date)
        entry.trade_code = request.POST.get('trade_code', entry.trade_code)
        entry.high = request.POST.get('high', entry.high)
        entry.low = request.POST.get('low', entry.low)
        entry.open = request.POST.get('open', entry.open)
        entry.close = request.POST.get('close', entry.close)
        entry.volume = request.POST.get('volume', entry.volume)
        # Update other fields as needed
        entry.save()

        return redirect('homepage')  # Redirect to the stock table after updating

    return render(request, 'edit_stock_entry.html', {'entry': entry})
