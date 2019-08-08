from django.shortcuts import render, redirect
from theapp.models import Account,Role,AccountRole
import json
from django.http import HttpResponse, HttpResponseRedirect
import sys

# Create your views here.
def index(request):
    if request.method == "POST":
        payload = request.POST.dict();

        entry = ""
        try:
            entry = Account.objects.get(username=payload['username'])
        except:
            print("Oops!",sys.exc_info()[0],"occured.")

        if entry:
            created = Account.objects.filter(username=payload['username']).update(password=payload['password'],build_status="null",infra_status="null")
        else:
            created = Account.objects.create(username=payload['username'],
                                            email=payload['username'],
                                            password=payload['password'],
                                            created_on='1997-03-28 00:00:00',
                                            last_login='1997-03-28 00:00:00')

        return redirect('theapp:index')
    elif request.method == "GET":
        users_list = Account.objects.order_by('user_id')
        role_list = Role.objects.order_by('role_id')
        accRole_list = AccountRole.objects.order_by('user_id')
        dict_dict = {"user_records":users_list, "role_records":role_list, "accrole_records":accRole_list}
        return render(request,'theapp/index.html',context=dict_dict)

def home(request):
    return render(request, 'theapp/home.html', context={})
