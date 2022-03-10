from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse

# Create your views here.
def TableTest(request):
    return render(request, 'table.html')

def Submit(request):
    return render(request, 'submit.html')

def test(request):
    r=request.body
    return render(request, 'index.html', {'r':r})

