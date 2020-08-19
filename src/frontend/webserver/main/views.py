from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    import os
    print('*\n' * 10)
    print(os.getcwd())
    print('*\n' * 10)
    return render(request, 'main/index.html')