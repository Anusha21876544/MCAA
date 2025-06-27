from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loder
 def maha(request):
     temp=loader.grt_template('maha.html')
     return HttpResponse(temp.renser)