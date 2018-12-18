from django.http import HttpResponse
from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def ws_test_page(request):
    return render(request, 'ws_test.html')
