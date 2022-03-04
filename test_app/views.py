from django.shortcuts import render
from test_main import settings
from django.core.mail import send_mail

# Create your views here.


def css(request):
    return render(request,'home.html')

def home(request):
    return render(request,'index.html')

def page(request):
    if request.method=='POST':
        subject=request.POST['to_sub']
        message=request.POST['to_mess']
        from_email=settings.EMAIL_HOST_USER
        mail=request.POST['to_mail']
        to_list=[mail]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return render(request,'page.html',{"info":"Message succesfully to "+mail[0:4]+'....'+mail[-10:]})
    return render(request,page.html)