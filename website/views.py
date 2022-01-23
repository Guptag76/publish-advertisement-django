import email
import os
from socket import herror
from django.shortcuts import render
from django.http import HttpResponse
import  json

from importlib_metadata import re
from pytz import NonExistentTimeError
from api import serializers
from api.models import Hero
from elitmus import *
from elitmus import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from api.models import Hero
from api.serializers import HeroSerializer
import requests

# Create your views here.
def index(request):
    return HttpResponse("hello world dfhurbrgbrh")





 
def add_data(request):
    print(request.POST)
    if request.user.is_anonymous:
        ht='<h1 style="text-align:center;">Please Login First For Create Any Post</h1>'
        return HttpResponse(ht)
    else:
        if len(request.POST)==0:
            print("enter in the page")
        else:
            if request.POST["my_post"]:
                post=request.POST["my_post"]
                email=request.user.email
                add_new_post(email,post)
            else:
                print("no data enter")
        email=request.user.email
    data=open_data_from_rest()
    return render(request,'add_data.html',{'data':data,'email':email})


def index2(request):
    
    #add_comment("k@gm.c",2,"d","chut")
    
    
    #ans=dict()
    #with open(settings.STATIC_DIR+'/media/adver.json', 'r') as f:
        #data = json.load(f)
    
    #data=dict()
    #print(data)
    #data['x']=[i  for i in range(10)]
    #callapi=requests.get('http://127.0.0.1:8000/rest/heroes/')
    #result=callapi.json()
    
    # print(type(t[0]))
    # Hero.objects.all().delete()
    # p=Hero()
    
    # p.my_data=data
    # p.save()
    #edit_json(request)
    #save_in_restapi(data)
    #data=dict()
    #add_new_post("w@f.c","chumma dee na gee")
    #print(data)
    #data=dict()
    data=open_data_from_rest()
    
    return render(request,'index.html',{"data":data,'email':None})


def login_html(request):
    
    return render(request,'login.html')

def signup_html(request):
    return render(request,'signup.html')

def save_in_restapi(data):
    Hero.objects.all().delete()
    p=Hero()
    
    p.my_data=data
    p.save()
    

def open_data_from_rest():
    result=Hero.objects.all()
    val=HeroSerializer(result,many=True)
    data=val.data
    data=eval(data[0]['my_data'])
    return data
    



def add_email_in_json(email):
    with open(settings.STATIC_DIR+'/media/adver.json', 'r') as f:
        data = json.load(f)
    
    data[email]=[]
    with open(settings.STATIC_DIR+'/media/adver.json', 'w') as f:
        json.dump(data,f,indent=4)
        
    
    save_in_restapi(data)

def fokati(request):
    data=open_data_from_rest()
    if request.user.is_anonymous:
        return render(request,'index.html',{'data':data,'email':None})
        
    if "input_comment" in request.POST:
        cmt=request.POST["input_comment"]
        for user in request.POST:
            login_user=user 
            val=list(request.POST[user].split(","))
        #print(len(val),val)
        post_id=val[0]
        post_email=val[1]
        #print(post_email,post_id,login_user,cmt)
        add_comment(post_email,int(post_id),login_user,cmt)
        #print(request.user.email)
    elif len(request.POST)==0:
        login_user=request.user.email
    else:
        login_user=request.user.email
        for user in request.POST:
            login_user=user 
            id=request.POST[user]
        delete_from_rest(login_user,id) 
    data=open_data_from_rest()
    return render(request,'index.html',{'data':data,'email':login_user})
    


def signup(request):
    #print("hellooooooo")
    #print(request.POST)
    #print(request.POST.get('user_id'),request.POST.get('email'),request.POST.get('password'))
    try:
        with open(settings.STATIC_DIR+'/media/adver.json','r') as f:
            data = json.load(f)
    except:
        data={}
    if len(request.POST)==0:
        pass
    else:
        user=request.POST.get('user_id')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(email=email).exists() or User.objects.filter(username=user).exists():
            pass
        else:    
            
            with open(settings.STATIC_DIR+'/media/adver.json', 'w') as f:
                json.dump(data,f,indent=4)
            data=open_data_from_rest()
            user = User.objects.create_user(user, email, password)
            user.save()
            add_email_in_json(email)
        
    return render(request,'index.html',{'data':data,'email':None})

def my_logout(request):
    data=open_data_from_rest()
    logout(request)
    #print(request.user.email)
    
    return render(request,'index.html',{'data':data,'email':None})


def my_login(request):
    data=open_data_from_rest()
    email=None
    if len(request.POST)==0:
        if request.user.is_anonymous:
            #print(request.user)
            email=None
        else:
            email=request.user.email
        
    else:
        if User.objects.filter(email=request.POST.get('email')).exists():
            username = User.objects.get(email=request.POST.get('email')).username
            user=authenticate(username=username,password=request.POST.get('password'))
            #print(username)
            email=request.POST.get('email')
            if user is not None:
                login(request,user)
                #print(request.POST.get('email'),request.POST.get('password'))
                #print(request.user.email)
                #print(user.email)
                #data[request.POST.get('email')]=request.POST.get('password')
                return render(request,'index.html',{'data':data,'email':email})
            email=None
    return render(request,'index.html',{'data':data,'email':email})

def add_new_post(email,post):
    with open(settings.STATIC_DIR+'/media/adver.json', 'r') as f:
        data = json.load(f)
    if email in data:
        my_arr=data[email]
        if len(my_arr)==0:
            val=[0,post,[]]
        else:
            val=[max(my_arr)[0]+1,post,[]]
        data[email].append(val)
        with open(settings.STATIC_DIR+'/media/adver.json', 'w') as f:
            json.dump(data,f,indent=4)
    
        save_in_restapi(data)
    else:
        print("not in data")
        
def add_comment(post_email,post_id,user_email,comment):
    with open(settings.STATIC_DIR+'/media/adver.json', 'r') as f:
        data = json.load(f)
    my_arr=data[post_email]
    if len(my_arr)>0:
        for user_post in my_arr:
            if user_post[0]==post_id:
                cmt=[user_email,comment]
                user_post[2].append(cmt)
                with open(settings.STATIC_DIR+'/media/adver.json', 'w') as f:
                    json.dump(data,f,indent=4)
                save_in_restapi(data)
    
def delete_from_rest(user_email,post_id):
    with open(settings.STATIC_DIR+'/media/adver.json', 'r') as f:
        data = json.load(f)
    my_arr=data[user_email]
    for post in my_arr:
        if post[0]==int(post_id):
            my_arr.remove(post)
            #print("data delete")
    with open(settings.STATIC_DIR+'/media/adver.json', 'w') as f:
        json.dump(data,f,indent=4)
    save_in_restapi(data)
    




