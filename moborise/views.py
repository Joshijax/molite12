from django.shortcuts import render
from .models import uploads, Agent, UserType, Comment, Reply
from django.conf import settings
from django.contrib import messages 
from django.http import HttpResponse
from .forms import AgentForm, LoginUpForm, SignUpForm
from Agent.forms import AgentLoginUpForm, AgentSignUpForm
from Agent.models import Agentuploads
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.template import loader

# Create your views here.
def index(request):
    form = SignUpForm(data=request.POST)
    form2 = LoginUpForm(data=request.POST)
    # loading my forms
    tests = Agentuploads.objects.all().order_by('uploaded_at')

    paginator = Paginator(tests, 8)
    page = request.GET.get('page')
    tests = paginator.get_page(page)

   
    return render(request, 'home.html', {'tests': tests,'form2': form2,'form': form, 'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,})
@csrf_exempt
def load_index(request):
    page = request.POST.get('page')
    tests = Agentuploads.objects.all()

    paginator = Paginator(tests, 8)
    
    try:
        tests = paginator.page(page)
    except PageNotAnInteger:
        tests = paginator.page(2)
    except EmptyPage:
        tests = paginator.page(paginator.num_pages)

    post_html = loader.render_to_string('home_ajax.html', {'tests' : tests})

    output_data = {
        'post_html' : post_html,
        'has_next' : tests.has_next()
    }
    return JsonResponse(output_data)





    return render(request, 'home_ajax.html', {'tests': tests,'form2': form2,'form': form, 'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,})

def home(request):
    form = AgentForm(data=request.POST)
    tests = uploads.objects.all()
    context = {'tests': tests,'form': form, 'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'home_ajax.html'
    return render(request, template, context)

def loginreq(request):
    form = LoginUpForm(data=request.POST)
    tests = uploads.objects.all()
    context = {'tests': tests,'form': form, 'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'login_ajax.html'
    if request.method == 'POST': 
        form = LoginUpForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        passwordval = User.objects.filter(username=username, password=password)
        if user < 1:
            return JsonResponse({'username_error':'username Does not exist'})

        if passwordval < 1:
            return JsonResponse({'password_error':'password does not match'})

        user = authenticate(username=username, password=password)
              
        login(request, user)
        request.session['username'] = username

        return HttpResponse('successfully registered')

    return render(request, template, context)

def loginUser(request):
    if request.method == 'POST':
        form = LoginUpForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
       
            
        if not User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username Does not exist'})

        if not authenticate(username=username, password=password):
            return JsonResponse({'password_error':'password does not match'})

        user = authenticate(username=username, password=password)
                
        login(request, user)
        request.session['username'] = username
        if request.user.profile ==  'Agent':
            return JsonResponse({'success':'success',
            'user':'Agent'})
        return JsonResponse({'success':'success'})
        
        
    else:
        form = LoginUpForm()
      
    return render(request, 'login_ajax.html',  {'form': form,})


@csrf_exempt
def replyy(request):
     
    page = request.POST.get('page')
    print(page)
    comment = Comment.objects.filter(id=page)
    print(comment)
    context = {'comment': comment, 'media_url': settings.MEDIA_URL,}

    template = 'reply.html'
    
    return render(request, template, context)



def search(request):
    q = request.GET.get('q')
    print(q)
    query_string = "SELECT * FROM moborise_uploads WHERE location  LIKE %s ORDER BY id ASC"
    search = uploads.objects.raw(query_string, ('%' + q + '%',))
    
    if len(list(search)) > 0:
        messages.add_message(request, messages.SUCCESS, f'Result for search {q}')
    else:
        messages.warning(request, f'No Result for search {q}')
        
    return render(request, 'search.html',  {'search': search, 'media_url': settings.MEDIA_URL,})

def NewUser(request):
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
        profile.role = 'user'
        profile.save()
    
        
        return JsonResponse({'success':'success'})


@csrf_exempt
def comment(request, property_id, username):
    comment = request.POST['comment']
    time = request.POST['time']
    user = Comment.objects.create(
            text = comment,
            time= time,
            post_id = property_id,
            author = request.user,
            to = username,
            Username = request.user.get_full_name(),
            
        )
    
    
    post_html = loader.render_to_string('comment.html', {'comment' : user})

    output_data = {
        'post_html' : post_html,
    }
    return JsonResponse(output_data)

@csrf_exempt
def send_reply(request, comment_id, username):
    reply = request.POST['comment']
    time = request.POST['time']
    print(reply)
    user = Reply.objects.create(
            reply = reply,
            time= time,
            rep_id = comment_id,
            Username = request.user.get_full_name(),
            to = username,
        
        )
    
    
    post_html = loader.render_to_string('send_reply.html', {'comment' : user})

    output_data = {
        'post_html' : post_html,
    }
    return JsonResponse(output_data)

@csrf_exempt
def commentlist(request, property_id, username):

    comment = Comment.objects.filter(post_id=property_id)
    post_html = loader.render_to_string('comment.html', {'comment' : comment})

    output_data = {
        'post_html' : post_html,
    }
    return JsonResponse(output_data)



def show_property(request, property_id, username):
    form = SignUpForm(data=request.POST)
    form2 = LoginUpForm(data=request.POST)
    user = get_object_or_404(User, username=username,)
    
    propertyy = Agentuploads.objects.get(id=property_id)
    comment = Comment.objects.filter(post_id=property_id)
    
    return render(request, 'view_property.html', {'form2': form2,'comment': comment,'form': form,"person":user,'property': propertyy, 'media_url': settings.MEDIA_URL,})








def signup(request):
    form = SignUpForm(data=request.POST)
    tests = uploads.objects.all()
    context = {'tests': tests,'form': form, 'media_url': settings.MEDIA_URL, 'media_root': settings.MEDIA_ROOT,}
    template = 'signup.html'
    

    return render(request, template, context)

def logout_request(request):
    
    
    
    logout(request)
    
    return redirect('/')
