from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'index.html', {'ism': 'ALI'})
 
def main(request):
  return HttpResponse("Waalaykum assalom")  

