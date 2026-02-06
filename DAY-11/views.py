from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import Inputform

from .models import SignUp, user, formModel, LoginUser

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def userlist(request):
    users = user.objects.all().values() 
    template = loader.get_template('userlist.html')
    context = {
        'users': users,

    }
    return HttpResponse(template.render(context, request))



def home_view(request):
    context={}
    context['form']=Inputform()
    return render(request, "about/student_registration.html", context)



def form_view(request):
    if request.method=='POST':
        print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
        context = {
            'title': title,
            'description': description,
        }
        form = formModel(title=title, description=description)
        form.save()
        return render(request, "form.html", context)
    return render(request, "form.html")




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = None
        try:
            user = SignUp.objects.get(username=username, is_active=True)
        except SignUp.DoesNotExist:
            try:
                user = LoginUser.objects.get(username=username, is_active=True)
            except LoginUser.DoesNotExist:
                user = None
                
        if user and user.check_password(password):
            return redirect('about')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, "login.html")


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not password or not email:
            messages.error(request, 'All fields are required.')
            return redirect('signup')
        
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('signup')
        
        if SignUp.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')
        
        if SignUp.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')
        


        user = SignUp(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, "signup.html")