from django.shortcuts import render
from .models import Account

def account_info(request):
    account = Account.objects.first()
    context = {
        'account': account
    }
    return render(request, 'banking/account_info.html', context)
