from django.shortcuts import render
from django.contrib import messages
from .models import Stock
from .forms import StockCreateForm, StockSearchForm

# Create your views here.
def list_item(request):
	queryset = Stock.objects.all()
	form = StockSearchForm(request.POST or None)
	context = {
		"queryset": queryset,
		"form": form
		}
	if request.method == 'POST':
    		queryset = Stock.objects.filter(item_no__icontains=form['item_no'].value(),color__icontains=form['color'].value(),)
    		context = {
		"queryset": queryset,
		"form": form
		}
				
	return render(request, "store/list_store.html", context)

def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		item = form.cleaned_data.get("item_no")
		color = form.cleaned_data.get("item_no")
		size = form.cleaned_data.get("size")
		form.save()
		messages.info(request,f"Item {item} {color} {size} MTS Successfuly created" )
		return redirect('list')
	context = {
		'form': form
	}
	return render (request, "store/add_items.html", context)




def home(request):
	return render(request, 'store/home.html')
