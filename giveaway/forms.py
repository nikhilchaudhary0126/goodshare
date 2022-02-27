from django import forms
from giveaway.models import Food, Clothes

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
CONDITION_CHOICES = [
    ('Poor', 'Poor'),
    ('Fair', 'Fair'),
    ('Good', 'Good'),
    ('New', 'New')
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

class ClothesForm(forms.ModelForm):

    class Meta:
        model = Clothes
        fields = ('size', 'gender', 'condition', 'address', 'city', 'state', 'contactno', 'description','pickupdate')

        # create a widegets dictionary
        widget = {
            'size': forms.Form(forms.ChoiceField(choices=SIZE_CHOICES)),
            'gender': forms.Form(forms.ChoiceField(choices=GENDER_CHOICES)),
            'condition': forms.Form(forms.ChoiceField(choices=CONDITION_CHOICES)),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'contactno': forms.TextInput(attrs={'class': 'form-control'}),
            'pickupdate': forms.DateField(widget=forms.SelectDateWidget()),
        }