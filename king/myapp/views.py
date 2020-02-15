from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views import View
from django.core.paginator import Paginator
from .models import *
# Create your views here.
import json


class RegisterView(View):
    def post(self,request):
        print(request.POST)
        name=request.POST.get('name')
        price=request.POST.get('price')
        num=request.POST.get('num')
        user=GOODS.objects.filter(name=name).first()
        if user:
            return HttpResponse(json.dumps({'msg':'该商品已存在','code':404}))
        else:
          
            user=GOODS.objects.filter(name=name,price=price,num=num).first()
            return HttpResponse(json.dumps({'msg': '添加成功', 'code': 200}))
           







class UserShowView(View):
    def get(self,request):


        good=GOODS.objects.all()
        good_list=[]
        for i in good:
            good_list.append({
                'id':i.id,
                'name':i.name,
                'price':i.price,
                'num':i.num,


            })
        return HttpResponse(json.dumps({'msg':'OK','code':200,'good':good_list}))



