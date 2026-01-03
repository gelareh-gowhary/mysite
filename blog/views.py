from django.shortcuts import render ,get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1)
    if kwargs.get('cat_name') !=None :
        posts=posts.filter(category__name=kwargs['cat_name'] )
    if kwargs.get('author_username') !=None:
        posts=posts.filter(author__username=kwargs['author_username'])    
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
    

def blog_single(request,pid):
      posts=Post.objects.filter(status=1)
      post=get_object_or_404(posts,id=pid)
      context={'post':post}
      return render(request,'blog/-single.html',context)
def test(request,pid):
    #   posts=Post.objects.all()
    #   post=Post.objects.get(id=pid)
      post=get_object_or_404(Post,id=pid)
    #   posts=Post.objects.all().filter(status=1)
    #   context={'posts':posts}
    #   context={'name':name,'family_name':family_name,'age':age}
      context={'post':post}

      return render(request,'test.html',context)
def test2(request):
     return render(request,'test2.html')
     

def blog_category(request,cat_name):
      posts=Post.objects.filter(status=1)
      posts=posts.filter(category__name=cat_name)
      context={'posts':posts}
      return render(request,'blog/blog-home.html',context)


     
          