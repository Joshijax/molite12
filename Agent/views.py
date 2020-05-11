from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages 
from django.http import HttpResponse
from moborise.models import  ProfilPicx
from .models import Agentuploads, uploadsfile
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import AgentUploadFileForm, AgentSignUpForm, ProfileUploadForm
import os
from moborise.forms import LoginUpForm
from moborise.models import UserType, Comment
from django.contrib.auth.decorators import login_required
 
# Create your views here.
def  SignupAgent(request):
    if request.method == 'POST':
        form = AgentSignUpForm(data=request.POST, initial={'role': request.user.UserType.role}, \
                            instance=request.user.UserType)
        
        password1 = request.POST['password']
        password = make_password(password1)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username already exists'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'email already in use'})
        
        if len(password1) < 5:
            return JsonResponse({'password_error':'password should be greater than 5'})
        
        if form.is_valid() :
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            
            user.save()
            user.userprofile.save()
        
        return JsonResponse({'success':'success'})
    else:

        form = AgentSignUpForm(data=request.POST,)
        form2 = LoginUpForm(data=request.POST)
    
   
    return render(request, 'AgentSignup.html', {'form2': form2,'form': form, 'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,})

def loginUser(request):

    form = LoginUpForm()
      
    return render(request, 'login_ajaxAgent.html',  {'form': form,})



@login_required(login_url='/')
@csrf_exempt
def upload_profilePicx(request, user_id):
    

    if request.user.is_authenticated == True:
        user = request.user
        print(user)
       
        tests = ProfilPicx.objects.get(user_id = user_id,)
        tests.delete()
        if request.method == 'POST':
            obj = User.objects.get(id=user_id)
            form = ProfileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                obj = User.objects.get(id=user_id)
                profile = obj.profilePicx
                profile.img = form.cleaned_data['img']
                profile.save()
                
            print('N')
            messages.add_message(request, messages.SUCCESS, 'Profile Picx Uploaded')
            
            return redirect('Agent:Agentupdate')
        return redirect('home')
    else:
        form = ProfileUploadForm()
    messages.add_message(request, messages.SUCCESS, 'Error')
    return redirect('home')  

@login_required(login_url='/')
@csrf_exempt
def UpdateProfile(request, user_id,):
    
    if request.method == 'POST':
        About = request.POST['about']
        Phone = request.POST['phone']
        Whatsapp_num = request.POST['whatsapp_num']
        Business_name = request.POST['business_name']
        Employment_stat = request.POST['employment_stat']
        
        print(Whatsapp_num)

        obj = User.objects.get(id=user_id)

        obj.profile.About=About
        obj.profile.phone=Phone
        
        obj.profile.whatapp_number=Whatsapp_num
        obj.profile.Business_Name=Business_name
        obj.profile.Employment_status=Employment_stat

        obj.profile.save()

      
    return render(request, 'login_ajaxAgent.html', )

@login_required(login_url='/')
def AgentHome(request):
    
    
   
    return render(request, 'Agent.html', {'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,})
@login_required(login_url='/')
def Agentupload(request):
    form = AgentUploadFileForm(data=request.POST)
    tests = User.objects.all()
    context = {'tests': tests,'media_url': settings.MEDIA_URL,'form': form, 'media_root': settings.MEDIA_ROOT,}
    template = 'upload.html'

    

    return render(request, template, context)
@login_required(login_url='/')
def Agentupdate(request):
    form = ProfileUploadForm(data=request.POST)
    tests = User.objects.get(username=request.user)
    listing = Agentuploads.objects.filter(username=request.user)
    context = {'tests': tests,'listing': listing, 'form': form,'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'update.html'
    

    return render(request, template, context)

@login_required(login_url='/')
def Agenthome(request):
    
    tests = User.objects.all()
    context = {'tests': tests,'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'Agenthome.html'
    

    return render(request, template, context)
@login_required(login_url='/')
def ekosodin(request):
    
    tests = Agentuploads.objects.all().filter(username = request.user, property_Location='Ekosodin')
    context = {'tests': tests,'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'listings/ekosodin.html'
    

    return render(request, template, context)


@login_required(login_url='/')
def osasoge(request):
    
    tests = Agentuploads.objects.all().filter(username = request.user, property_Location='Osasoge')
    context = {'tests': tests,'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'listings/osasoge.html'
    

    return render(request, template, context)


@login_required(login_url='/')
def bdpa(request):
    
    tests = Agentuploads.objects.all().filter(username = request.user, property_Location='BDPA')
    context = {'tests': tests,'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'listings/bdpa.html'
    

    return render(request, template, context)
def show_Agentproperty(request, property_id, username):
    
    user = get_object_or_404(User, username=username,)
    
    propertyy = Agentuploads.objects.get(id=property_id)
    comment = Comment.objects.filter(post_id=property_id)
    
    return render(request, 'view_agentUpload.html', {'comment': comment,"person":user,'property': propertyy, 'media_url': settings.MEDIA_URL,})

@login_required(login_url='/')
def upload_file(request):
    

    if request.user.is_authenticated == True:
        user = request.user
        print(user)
        if request.method == 'POST':
            form = AgentUploadFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            
            if form.is_valid():
                new_obj = Agentuploads(file=form.cleaned_data['file'],property_Name=request.POST['property_Name'], property_Location=request.POST['property_Location'] , property_Type=request.POST['property_Type'], property_Description=request.POST['property_Description'], property_Address=request.POST['property_Address'], username=user, author=request.user)
                new_obj.save()

                for f in files:
                    gallery = uploadsfile(post=new_obj, file=f)
                    gallery.save()
                messages.add_message(request, messages.SUCCESS, 'image succesfully uploaded')
                return redirect('Agent:Agentupload')
            else:
                print(request.POST)
                print(form.errors)
                print(form.non_field_errors)
                return redirect('index')
        
    else:
        form = AgentUploadFileForm()
    messages.add_message(request, messages.SUCCESS, 'Error')
    return redirect('home')  


@login_required(login_url='/')
def NewAgent(request):
    if request.method == 'POST':
        
        
        firstname = request.POST['name']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password = make_password(password1)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username already exists'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'email already in use'})
        
        if len(password1) < 5:
            return JsonResponse({'password_error':'password should be greater than 5'})
        
        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username,
            email = email,
            password = password,
            
        )
        user =  User.objects.get(username=request.POST['username'],)
        
        profile = user.profile # because of signal and one2one relation
        
        profile.role = 'Agent'
        profile.save()
    
        
        return JsonResponse({'success':'success'})

@login_required(login_url='/')
def delete(request, id_image):
    user = request.user
    file_type = 'image'
   

    testss = Agentuploads.objects.get(id = id_image,)
    testss.delete()

    # messages.add_message(request, messages.SUCCESS, f'image {file_name} successfully deleted')
    return redirect('Agent:Agentupload')
