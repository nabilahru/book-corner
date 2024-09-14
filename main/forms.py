from django.forms import ModelForm
from main.models import DataProduct

class DataProductForm(ModelForm):
    class Meta:
        model = DataProduct
        fields = ["name", "price", "genre_category", "quantity", "description"]