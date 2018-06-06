# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import Book

def index(request):
    
    return render(request,'product_app/index.html')

def submit_survey(request):
    if request.method == "POST":
        Book.objects.create(title_name=request.POST['title_name'], author_name= request.POST['author_name'], category_name= request.POST['category_name'])
    return redirect('/result')
      
def result(request):
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'product_app/submitted.html', context)


      
       

