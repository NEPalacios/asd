from django.shortcuts import render
from .models import Stock

def home_view(request):
    return render(request, 'core/index.html')

def stock_view(request):
    if request.method == 'GET':
        return render(request, 'core/formulario_stock.html')
    else:
        from .models import Stock
        mi_stock = Stock(producto=request.POST['producto'],
                         cantidad=request.POST['cantidad'])
        mi_stock.save
    
    
        return render(request, 'core/formulario_stock.html')
    