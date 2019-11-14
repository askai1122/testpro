from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from firrst_app.forms import RegistrationForm
# Create your views here.
from django.contrib.auth.models import User,auth
# from .models import Mypost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post,Topic,Webpage,AccessRecord
from willflyy import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# @method_decorator(login_required, name="dispatch")
def index(request):

	return render(request, 'willflyy/index.html')

def webpage(request): 
    webpage_list = Webpage.objects.order_by('name')

    ar_dict1 = {'webpage' : webpage_list}

    return render(request, 'willflyy/acces_record.html', context=ar_dict1)
    
@login_required(login_url='login')
def myprofile(request):
    return render(request, 'willflyy/myprofile.html')
def secondpage(request):
    context_dict = {'text' : 'hello world', 'number':100}

    return render(request, 'willflyy/2ndpage.html', context_dict)
def thirdpage(request):
    return render(request, 'willflyy/thirdpage.html')

def accessrecord(request): 
    # access_record_list = AccessRecord.objects.order_by('date')
    # webpage_list = Webpage.objects.order_by('name')

    # ar_dict = {'access_record': access_record_list, 'webpage' : webpage_list}

    return render(request, 'willflyy/post.html',)

def contactus(request):
	return render(request, 'willflyy/contactus.html')

def upload_profile(request):
	return render(request, 'willflyy/Upload_image.html')

def help(request):
	return render(request, 'willflyy/help.html')

def aboutus(request):
	return render(request, 'willflyy/aboutus.html')	


@login_required(login_url='login')
def home(request):
    
	return render(request,'willflyy/home.html');


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        

        if form.is_valid():
            # do something
            print("Form Validation success. Prints in console.")
            print("first_name: "+form.cleaned_data['first_name'])
            print("last_name: "+form.cleaned_data['last_name'])

            print("Email: "+form.cleaned_data['email'])
            print("Password: "+form.cleaned_data['password'])
            

            try:



                user = User.objects.get(username=request.POST['user_name'])
                return render(request, 'willflyy/register.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                p = request.FILES['uploadprofile'];
                from .models import profile
                u = profile(pic=p);
                u.save();

                user = User.objects.create_user(email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],username= request.POST['user_name'],password= request.POST['password'])

                auth.login(request, user)
                return redirect(login)
                   

            # print("Text: "+form.cleaned_data['text'])

    return render(request, 'willflyy/register.html',{'form':form})


# def register(request):
#     if request.method == "POST":

#         # if request.POST['username'] == ['']:

#             # if request.POST['first_name'] == request.POST['password']:
    
#                     if request.POST['password'] == request.POST['passwordagain']:

#                         try:
#                             user = User.objects.get(username=request.POST['username'])
#                             return render(request, 'willflyy/register.html', {'error': "Username Has Already Been Taken"})
#                         except User.DoesNotExist:
                            # user = User.objects.create_user(email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],username= request.POST['username'],password= request.POST['password'])
                            # # p = request.FILES['images'];
                            # # from .models import profile
                            # # u = profile(pic=p);
                            # # u.save();
                            # auth.login(request, user)
                            # return redirect(login)
#                     else: 
#                         return render(request, 'willflyy/register.html', {'error': "Passwords Don't Match"})
      

            # else:
                # return render(request, 'willflyy/register.html', {'error': "Password is similiar to your name"})        

          
        # else:

            # return render(request, 'willflyy/register.html', {'error': "Everything must be valid"})   
           

    # else:
    #     return render(request, 'willflyy/register.html')

def login(request):
    if request.method == "POST":
        # check if a user exists
        # with the username and password
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'willflyy/index.html', {'error': "Invalid Login credentials."})
    else:
        return render(request, 'willflyy/index.html')

def logout(request):
    auth.logout(request)
    return redirect(login)


def newpost(request):
    return render(request, 'willflyy/new_post.html')




