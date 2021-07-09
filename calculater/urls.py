from django.urls import  path
from . import  views
#这个app的urls,可以向这里索引
urlpatterns=[
    path('',views.main),
    path('index',views.index,name='index'),
    path('calpage',views.calpage,name='calpage'),
    path('result',views.oprate,name='result'),
    path('callist',views.callist,name='callist')
]
