from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms
from first_app.forms import NewUserForm
# Create your views here.

def index(request):
    con_dict = {'text':'hello world','number':100}
    return render(request,'first_app/index.html',context=con_dict)

def other(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/other.html',context=date_dict)

def relative_url_templates(request):
    return render(request,'first_app/relative_url_templates.html')


#def users(request):
#    user_list = User.objects.order_by('first_name')
#    user_dict = {"users_records":user_list}
#    return render(request,'first_app/users.html',context=user_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users_records":user_list}
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'first_app/users.html',{'form':form, "users_records":user_list})

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation")
            print("Name : " +form.cleaned_data['name'])
            print("Email : " +form.cleaned_data['email'])
            print("Text : " +form.cleaned_data['text'])
    return render(request,'first_app/form_page.html',{'form':form})
