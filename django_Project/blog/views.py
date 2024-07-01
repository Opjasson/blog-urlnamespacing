from django.shortcuts import render

from .models import Post
def index(request):
    post = Post.objects.all
    context = {
        'judul' : 'Ini adalah halaman blog',
        'isi'   : post
    }
    return render(request,'blog.html',context)

def slugyfy(request,judulurl):

    categories = Post.objects.values('category').distinct
    posts = Post.objects.get(judul = judulurl)
    context = {
        'judul' : 'Ini adalah halaman blog',
        'post'   : posts,
        'category' : categories
    }
    return render(request,'detail.html',context)

def category(request,categoryurl):
    
    categories = Post.objects.values('category').distinct
    post = Post.objects.filter(category = categoryurl)
    context = {
        'judul' : 'Pilih Berdasarkan Category',
        'postingan'   : post,
        'category'  : categories
    }
    return render(request,'category.html',context)