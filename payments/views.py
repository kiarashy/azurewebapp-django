from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

def home(request):
    payments = Payment.objects.all().order_by('-id')  # Get all payments, newest first
    return render(request, 'payments/home.html', {'payments': payments})


def payment_form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment-form')
    else:
        form = PaymentForm()

    payments = Payment.objects.all().order_by('-id')  # newest first
    return render(request, 'payments/form.html', {
        'form': form,
        'payments': payments
    })
