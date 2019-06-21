from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Topic, Webpage, AccessRecord, MyUser, UserProfileInfo
from first_app.forms import NewUserForm,UserForm,UserProfileInfoForm


from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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
#    user_list = MyUser.objects.order_by('first_name')
#    user_dict = {"users_records":user_list}
#    return render(request,'first_app/users.html',context=user_dict)

def users(request):
    user_list = MyUser.objects.order_by('first_name')
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

def registration(request):
    registered = False
    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # Now we deal with the extra info!
            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']
            # Now save model
            profile.save()
            # Registration Successful!
            registered = True
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("INVALID Login details supplied")
    else:
        return render(request, 'first_app/login.html',{})
