from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Assalamu alaykum")

def main(request):
  return HttpResponse("Waalaykum assalom")  
