from django.db import models


class Stock(models.Model):
    item_no = models.CharField(max_length=50, blank=False, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=False, null=True)
    color = models.CharField(max_length=50, blank=False, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    export_to_CSV = models.BooleanField(default=False)
    # date = models.DateTimeField(auto_now=False, auto_now_add=False)
    

    def __str__(self):
        return f'Item: {self.item_no} | Color: {self.color}'

