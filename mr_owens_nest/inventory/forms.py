from django.forms import ModelForm
from .models import InventoryItems

class AddItems(ModelForm):
    class Meta:
        model = InventoryItems
        fields = '__all__'
        exclude = ['slug', 'date_added', 'date_updated']