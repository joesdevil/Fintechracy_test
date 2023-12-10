# receipts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt
from .forms import ReceiptForm , RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
 
from django.contrib.auth.views import LoginView, LogoutView



# registration view
 

def register(request):
    #making post request for user reg
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to your login page
            return redirect('/login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Logout view
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to home page after logout

# Use Django's built-in LoginView for login
login_view = LoginView.as_view(template_name='registration/login.html')

# Decorator to ensure only authenticated users can access certain view
@login_required(login_url='login')
def home(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipts/home.html',{"receipts":receipts})



#view list -- we can use other method 'ListView' class
@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipts/receipt_list.html', {'receipts': receipts})


#detail view -- we can use other method 'DeatilView' class
@login_required
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    return render(request, 'receipts/receipt_detail.html', {'receipt': receipt})



#add receipt
@login_required
def receipt_new(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_detail', pk=receipt.pk)
    else:
        form = ReceiptForm()
    return render(request, 'receipts/receipt_form.html', {'form': form})


# edit edit receipts 
@login_required
def receipt_edit(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    if request.method == "POST":
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_detail', pk=receipt.pk)
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, 'receipts/receipt_form.html', {'form': form})
