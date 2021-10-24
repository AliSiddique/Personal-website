from django.shortcuts import render
from .models import job, contactStuff
from django.core.exceptions import ValidationError

from django.http import HttpResponse

# Create your views here.





def home(request):
    context = {
           'posts': job.objects.all()
    }
    return render(request, 'blog/home.html', context)




def about(request):


    return render(request, 'blog/about.html')




def skills(request):
    return render(request, 'blog/skills.html')


def contact( request):
    if request.method == "POST":
        Contact = contactStuff()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.name = name
        Contact.email = email
        Contact.message = message
        Contact.save()
        return HttpResponse("<h1>Thanks</h1>")

    return render(request, 'blog/contact.html')
