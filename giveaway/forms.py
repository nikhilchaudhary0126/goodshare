from django import forms
from giveaway.models import Food

TYPE_CHOICES = [
    ('grocery', 'Grocery'),
    ('bakery', 'Bakery'),
    ('grains', 'Grains'),
    ('veggies', 'Veggies'),
    ('fruits', 'Fruits'),
    ('grains', 'Grains'),
    ('fresh produce', 'Fresh Produce')
]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('contactno', 'address', 'city', 'state', 'quantity', 'type', 'expiry', 'description')

        # create a widegets dictionary
        widget = {
            'contactno': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Form(forms.ChoiceField(choices=TYPE_CHOICES)),
            'image': forms.FileField(),
            'expiry': forms.DateField(),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
