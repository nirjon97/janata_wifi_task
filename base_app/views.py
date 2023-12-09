from django.shortcuts import render, get_object_or_404,redirect
from .models import StockData
from django.http import JsonResponse
from django.views import View
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

#this term is for api
class StockDataView(View):
    def get(self, request, *args, **kwargs):
        # Fetch all stock data from the database
        stock_data = StockData.objects.all().values()

        # Convert the QuerySet to a list of dictionaries
        stock_data_list = list(stock_data)

        # Return the data as JSON response
        return JsonResponse(stock_data_list, safe=False)
    


def another_visualization(request):
    stock_data = StockData.objects.all()

    context ={
        'stock_data': stock_data
    }
    return render(request,'another_visualization.html',context)