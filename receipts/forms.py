# receipts/forms.py
from django import forms
from .models import Receipt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#user reg form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



#receipt form
class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['store_name', 'date_of_purchase', 'item_list', 'total_amount']
        widgets = {
            'date_of_purchase': forms.DateInput(attrs={'type': 'date'}),
        }


