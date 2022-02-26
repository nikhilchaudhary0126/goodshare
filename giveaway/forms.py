from django import forms
from giveaway.models import Food

TYPE_CHOICES = [
    ('Grocery', 'Grocery'),
    ('Bakery', 'Bakery'),
    ('Grains', 'Grains'),
    ('Veggies', 'Veggies'),
    ('Fruits', 'Fruits'),
    ('Grains', 'Grains'),
    ('Fresh Produce', 'Fresh Produce')
]

SIZE_CHOICES = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL')
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Gender Neutral', 'Gender Neutral'),
    ('Any', 'Any')
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

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ('name', 'quantity', 'type', 'condition', 'description', 'contactno', 'latitude', 'longitude')

        # create a widegets dictionary
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Form(forms.ChoiceField(choices=TYPE_CHOICES)),
            'condition': forms.DateField(widget=forms.SelectDateWidget()),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'contactno': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
        }