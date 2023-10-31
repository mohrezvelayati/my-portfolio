from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def index_view(request):
    about = About.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    context = {'about':about, 'services':services, 'projects':projects}
    if request.method == "post":
        form = ContactForm(request.post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited sucessfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket did not submited ')

    return render(request, 'include/index.html', context)



# def contact_view(request):
#     return render(request, 'include/contact.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request,'Thanks for contacting us! We will get back to you soon')
            return HttpResponse('done')
        else:
            messages.info(request,'Some error in saving form!')
            return redirect('/')
    else:
        form = ContactForm()
        return render(request,'iclude/index.html', {'form': form})