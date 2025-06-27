from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def anusha(request):
    temp=loader.get_template('anusha.html')
    return HttpResponse(temp.render())

def day2(request):
    temp=loader.get_template('day2.html')
    return HttpResponse(temp.render()) 


def day3(request):
    temp=loader.get_template('day3.html')
    return HttpResponse(temp.render())  

def day4(request):
    temp=loader.get_template('day4.html')
    return HttpResponse(temp.render())  

     
def day5(request):
    return HttpResponse("day5") 
def day6(request):
    return HttpResponse("day6") 
def day7(request):
    return HttpResponse("day7") 
def day8(request):
    return HttpResponse("day8")
def day9(request):
    return HttpResponse("day9") 
def day10(request):
    return HttpResponse("day10") 
def day11(request):
    return HttpResponse("day11") 
def day12(request):
    return HttpResponse("day12") 
def day13(request):
    return HttpResponse("day13") 
def day14(request):
    return HttpResponse("day14") 
def day15(request):
    return HttpResponse("day15")  