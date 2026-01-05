from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse ,JsonResponse ,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request,messages.SUCCESS,'your ticket submited succefully')       
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submited ')       

    form=ContactForm()        
    return render(request,'website/contact.html',{'form':form})

def test_view(request):

    return render(request,'website/test.html',{'name':'gelareh','lastname':'gowhary'})


def formtest(request):
    if request.method == "POST":
        form = ContactForm(request.POST) #داده های وردی را دریافت میکنیم به ازای کانتکت فرم 
        if form.is_valid():
            form.save()
            # name=form.cleaned_data['name']
            # subject=form.cleaned_data['subject']
            # email=form.cleaned_data['email']
            # message=form.cleaned_data['message']
            # print(name,subject,email,message)
            return HttpResponse('done')
        else:
            return HttpResponse('notvalid')
        # name=(request.POST.get('name'))
        # print(name)
        # email=(request.POST.get('email'))
        # subject=(request.POST.get('subject'))
        # message=(request.POST.get('message'))
        # # print(name,email,subject,message)
        # c=Contact()
        # c.name=name
        # c.email=email
        # c.subject=subject
        # c.message=message
        # c.save()
    form = ContactForm()
    return render (request,'formtest.html',{'form':form})


def newsletter_view(request):
    if request.method=='POST':
        form=NewsletterForm(request.POST)#داده ورودی که توی ویو میخایم دریافت کنیم 
        if form.is_valid():
            form.save()           
            return HttpResponseRedirect('/') #ریدایرکت بشه به صفحه اصلی 
    else:
        return HttpResponseRedirect('/') 