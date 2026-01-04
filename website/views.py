from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse ,JsonResponse
from website.models import Contact
from website.forms import NameForm
def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')

def test_view(request):

    return render(request,'website/test.html',{'name':'gelareh','lastname':'gowhary'})

def  formtest_view(request):
    if request.method == 'Post':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('done')
        #   name = request.POST.get('name')
        #   print(name)
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        # c = Contact()
        # c.name = name
        # c.email = email
        # c.subject = subject
        # c.message = message
        # c.save()
        # print(c.name,c.email,c.subject,c.message)
    
    form=NameForm()    
    return render(request,'formtest_view.html',{'form':form}) 


