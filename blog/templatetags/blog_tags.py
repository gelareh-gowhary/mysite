from django import template
from blog.models import Post
from blog.models import Category,Comment


register=template.Library()

@register.simple_tag(name='totalpost')
def function():
    posts=Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts=Post.objects.filter(status=1)
    return posts
@register.simple_tag(name='comments_count')
def function(pid):
    # post=Post.objects.get(id=pid)#اول چک میکنیم که ایا پسته وجود داره یا نه 
    return Comment.objects.filter(post=pid,approved=True).count()#اگه وجود داشت کامنتهاش رو دربیار 

@register.filter
def snippet(value,arg=100):
    return value[:arg] + "......"


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts=Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts} 


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}        


