from django.shortcuts import render, redirect
from django.views import View
from .models import Projects, Technologies
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
def home(request):
    return render(request,'portfolio/index.html')


class ViewProjects(View):


    def get(self, request, *args, **kwargs):

        projects = Projects.objects.all()
        tecnos = Technologies.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(projects, 6)

        projects_data = paginator.get_page(page_number)

        context = {
            'projects': projects_data,
            'tecnos': tecnos
        }

        return render(request, 'portfolio/projects.html',context)
    

class DetailViewProject(View):

    def get(self,request,slug,*args,**kwargs):

        project = Projects.objects.get(slug=slug)

        tecno = Technologies.objects.filter(projects=project)

        context = {
            'project':project,
            'tecnos':tecno
        }

        return render(request,'portfolio/detailProject.html', context)   


class FilterViewProjects(View):
    def get(self,request,pk,*args,**kwargs):
        projects = Projects.objects.filter(technologies__id=pk).order_by('-id')
        page_number = request.GET.get('page')
        paginator = Paginator(projects, 6)

        projects_data = paginator.get_page(page_number)

        context = {
            'projects': projects_data,
            'tecnos': Technologies.objects.all()
        }

        return render(request, 'portfolio/projects.html',context)


class ContactView(View):

    def get(self,request,*args,**kwargs):

        form = ContactForm()

        context = {
            'form':form
        }

        return render(request,'portfolio/contact.html',context)

    def post(self,request,*args,**kwargs):
        form = ContactForm(request.POST)    
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            email_send = form.cleaned_data['email_send']


            send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[email_send],fail_silently=True)

        messages.success(request,'Email send')

        return redirect('portfolio:home')