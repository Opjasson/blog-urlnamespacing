from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Home page'
    }
    return render(request,'index.html',context)