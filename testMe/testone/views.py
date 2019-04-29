from django.shortcuts import render
from .models import User
# Create your views here.
import random
from xpinyin import Pinyin

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
p=Pinyin()
def begin():
    a1=['张','金','李','王','赵']
    a2=['玉','明','龙','芳','军','玲']
    a3=['','立','玲','','国','']
    name=random.choice(a1)+random.choice(a2)+random.choice(a3)
    password=p.get_pinyin(name,"")
    return [name,password]



# def index(request):
    # User.objects.all().delete()
    # for i in range(10):
    #     p=begin()
    #     name,password=p
    #     User.objects.create(name=name,password=password)
    # users_list = User.objects.all()
    # paginator=Paginator(users_list,10)
    # page=request.GET.get("page")
    # try:
    #     users=paginator.page(page)
    # except PageNotAnInteger as identifier:
    #     users=paginator.page(1)
    # except EmptyPage:
    #     users=paginator.page(paginator.num_pages)
    # currentPage=page
    # return render(request,"index.html",{"users":users,"paginator":paginator,"currentPage":currentPage})

def index(request):
    user_list=User.objects.all()
    paginator=Paginator(user_list,10)
    page=request.GET.get("page")
    currentPage=page;

    try:
        users=paginator.page(page)
    except PageNotAnInteger as identifier:
        users=paginator.page(1)
    except EmptyPage:
        users=paginator.page(paginator.num_pages)
    users.paginator
    paginator.page_range
    return render(request,"index.html",{"users":users})
    




    