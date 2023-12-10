# receipts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt
from .forms import ReceiptForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
 
from django.contrib.auth.views import LoginView, LogoutView



# Custom registration view
class RegistrationView(LoginView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = '/'

# Logout view
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to home page after logout

# Use Django's built-in LoginView for login
login_view = LoginView.as_view(template_name='registration/login.html')

# Decorator to ensure only authenticated users can access certain views
@login_required(login_url='login')
def home(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipts/home.html',{"receipts":receipts})



@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipts/receipt_list.html', {'receipts': receipts})

@login_required
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    return render(request, 'receipts/receipt_detail.html', {'receipt': receipt})

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
