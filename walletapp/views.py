from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import AccountDetail, Transfer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.db.models import F

# Create your views here.

def login_user(request):
    logout(request)
    username = password = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'login.html')

class ProfileView(ListView):
    model = AccountDetail
    template_name = 'dashboard.html'
    context_object_name = 'dashboard'
    queryset = AccountDetail.objects.all()

    def get_context_data(self, **kwargs):

        context = super(ProfileView, self).get_context_data(**kwargs)
        context['account'] = AccountDetail.objects.all()
        
        return context




def transfer_view(request):
    current_user = request.user
    user_transfer = Transfer.objects.filter(sending_user=current_user)

    return render(request, 'trans_history.html', {'transfer': user_transfer})
        


def transfer(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['reciver_name']
        acct_num = request.POST['account_number']
        amount = request.POST['amount']
        desc = request.POST['desc']
        user = User.objects.get(username=username)
        model = Transfer.objects.create(sending_user=user, reciver_name=name, reciver_account=acct_num, amount=amount, desc=desc)
        if model:
            user_det = AccountDetail.objects.get(account_holder=user)
            user_det.account_balance = F('account_balance') - int(amount)
            user_det.save()
            model.save()
            context = {'bal': user_det.account_balance}

            return redirect('transfer')

    return render(request, 'transfer.html')

def contact(request):
    template = 'contact.html'
    return render(request, template)