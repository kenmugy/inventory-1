from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from .models import Stock
from .forms import *

from django.http import HttpResponse
import csv

# Create your views here.
@login_required
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
				if form['export_to_CSV'].value() == True:
					response = HttpResponse(content_type='text/csv')
					response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
					writer = csv.writer(response)
					writer.writerow(['ITEM NO', 'SIZE', 'COLOR'])
					instance = queryset
					for stock in instance:
						writer.writerow([stock.item_no, stock.size, stock.quantity])
					return response
				
	return render(request, "store/list_store.html", context)

@login_required
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

@login_required
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

class StockDeleteView(LoginRequiredMixin,DeleteView):
		model = Stock
		success_url = '/list'

class StockDetailView(LoginRequiredMixin,DetailView):
		model = Stock
@login_required
def issue_items(request, pk):
	queryset = get_object_or_404(Stock, id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		# instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_no) + "s now left in Store")
		instance.save()

		# return redirect('detail')
		return redirect('/'+str(instance.id)+'/detail')
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		# "title": 'Issue ' + str(queryset.item_no),
		"queryset": queryset,
		"form": form,
		# "username": 'Issue By: ' + str(request.user),
	}
	return render(request, "store/add_items.html", context)


@login_required
def receive_items(request, pk):
	queryset = get_object_or_404(Stock, id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_no)+"s now in Store")

		# return redirect('detail')
		return redirect('/'+str(instance.id)+'/detail')
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			# "title": 'Receive ' + str(queryset.item_no),
			"instance": queryset,
			"form": form,
			# "username": 'Receive By: ' + str(request.user),
		}
	return render(request, "store/add_items.html", context)
@login_required
def reorder_level(request, pk):
	queryset = get_object_or_404(Stock, id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_no) + " is updated to " + str(instance.reorder_level))

		return redirect("list")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "store/add_items.html", context)

def home(request):
	return render(request, 'store/home.html')
