from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
def main(request):
    return HttpResponse("register")
# Create your views here.
def main1(request):
    return render(request,'reg_index.html')
def send_email(request):
    subject=request.POST.get('subject','')
    message=request.POST.ger('message','')
    from_email=request.POST.get('from_email','')
    if(subject and message and from_email):
        try:
            send_mail(subject,message,from_email,['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('邮箱格式不正确')
        return HttpResponseRedirect('/register/main')
    else:
        return HttpResponse('确认填写是否到位')