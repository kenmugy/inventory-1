from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import DeleteView
from .models import Stock
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm

# Create your views here.
def list_item(request):
	queryset = Stock.objects.all().order_by('-last_updated')
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
		color = form.cleaned_data.get("color")
		size = form.cleaned_data.get("size")
		form.save()
		messages.success(request,f"Item {item} {color} {size} MTS Successfuly created" )
		return redirect('list')
	context = {
		'form': form
	}
	return render (request, "store/add_items.html", context)

def update_items(request, id):
			queryset = get_object_or_404(Stock, pk=id)
			form = StockUpdateForm(instance=queryset)
			if request.method == 'POST':
				form = StockUpdateForm(request.POST,instance=queryset)
				if form.is_valid():
						item = form.cleaned_data.get("item_no")
						form.save()
						messages.info(request,f"Item {item} Successfuly Update" )
						return redirect('list')
			return render(request, 'store/update_items.html',{'form': form})

class StockDeleteView(DeleteView):
    model = Stock
    success_url = '/list'

def home(request):
	return render(request, 'store/home.html')
