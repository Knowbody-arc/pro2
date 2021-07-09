from django.shortcuts import render
from django.http import HttpResponse
import json
from calculater.models import  cal
# Create your views here.
def main(request):
    return render(request,'main.html')
def index(request):
    return render(request,'index.html')
#第一个网站
def calpage(request):
    return render(request,'cal.html')
def oprate(request):
   a=int(request.POST['valueA'])
   b=int(request.POST['valueB'])
   op=request.POST['op']
   result=0
   if(op=='A'):
       result=a+b
   elif(op=='B'):
        result=a*b
   elif(op=='C'):
       if(b==0):
           result="Zero division error"
           return HttpResponse(result)
       else:
            result=a/b
   elif(op=='D'):
       result=a-b
   cal.objects.create(value_a=a,value_b=b,result=result)
   return render(request,'result.html',context={'data':result})
   #第三个是类似与字典的，让前端根据键来进行识别
def callist(request):
    data=cal.objects.all()
    return render(request,'show.html',context={'data':data})
def resultdel(request):
    cal.objects.all().delete()
    return HttpResponse('data deleted')

