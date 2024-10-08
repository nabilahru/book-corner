from django.forms import ModelForm
from main.models import DataProduct
from django.utils.html import strip_tags

class DataProductForm(ModelForm):
    class Meta:
        model = DataProduct
        fields = ["name", "price", "genre_category", "quantity", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_genre_category(self):
        genre_category = self.cleaned_data["genre_category"]
        return strip_tags(genre_category)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)