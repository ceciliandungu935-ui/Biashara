from django.shortcuts import render
from myapp.models import *



# Create your views here.
def index (request):
       if request.method =="POST":
          mycontact = Contact(
            name= request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
       )
          mycontact.save()
          return render(request, 'index.html')
       else:
            return render(request, 'index.html')
       

def error(request):
       return render (request, '404.html')

def blogdetails(request):
       return render (request, 'blog-details.html')

def blog(request):
       return render (request, 'blog.html')

def portfoliodetails(request):
       return render (request, 'portfolio-details.html')

def servicedetails(request):
       return render (request, 'service-details.html')

def starterpage(request):
       return render (request, 'starter-page.html')

def show(request):
      all= Contact.objects.all()
      return render(request, 'show.html', {'all': all})