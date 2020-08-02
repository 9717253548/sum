
import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Stock
import pandas as pd


# Create your views here.
# one parameter named request

def home(request):
   return render(request,"stock/stock_home.html")

def view_stock(request):
    stock= Stock.objects.filter(Dlr_Invoice_No="nan")
    context ={"stock":stock}
    return render(request,"stock/view_stock.html",context)

def stock_upload(request):
    # declaring template
    template = "stock/stock_upload.html"
    data = Stock.objects.all()
    prompt = {
        'order': 'Order of the CSV should be Chassis,Engineno and description ',
        'profiles': data    
              }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    x= pd.read_csv(csv_file,delimiter = ',')
    size = len(x)
    for i in range(size):
        b= Stock(
            Chassis_No=x['Chassis No.'][i],
        Engine_No=x["Engine No"][i],
        Description=x['Product Description'][i],
        Dlr_Invoice_No=x['Dlr Invoice No'][i],
        GST_Invoice = x['GST Invoice#'][i],
        Manufacturing_Date = x['Manufacturing Date'][i],
        TM_Invoice_Date = x['TM Invoice Date'][i],
        Commercial_Invoice = x['Commercial Invoice#'][i],
        Selling_Dealer = x['Selling Dealer'][i],
        Product = x['Product/VC#'][i],
        Dealer_Purchase_Order_Price = x['Dealer Purchase Order Price'][i],
        Product_Line = x['Product Line'][i],
        LOB = x['LOB'][i],
        Parent_Product_Line=x['Parent Product Line'][i]
            
        )
        b.save()        
    
    context = {}
    return render(request, template, context)