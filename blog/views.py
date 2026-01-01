from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request,'blog/blog-home.html')


def blog_single(request):
        
        context={'title':'bitcoin crached agian!','content':'bitcoin was flying but now grownded as always','author':'gelareh-gowhary'}

        return render(request,'blog/blog-single.html',context)