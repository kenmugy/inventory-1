from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
	
	class Meta:
		model = Stock
		fields = ["item_no", "size", "color", "quantity"]

	# def get_absolute_url(self):
	#     return reverse('list')
		# return reverse('list', kwargs={'pk': self.pk})

	def clean_item_no(self):
		item_no = self.cleaned_data.get("item_no")

		for instance in Stock.objects.all():
			if instance.item_no == item_no:
				raise forms.ValidationError(item_no + " already in Database")
		
		return item_no
	

class StockSearchForm(forms.ModelForm):
	item_no = forms.CharField(required=False)
	color = forms.CharField(required=False)
	export_to_CSV = forms.BooleanField(required=False)
	class Meta:
		model = Stock
		fields = ["item_no", "color"]


class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["item_no", "size", "quantity"]
	

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quantity']
