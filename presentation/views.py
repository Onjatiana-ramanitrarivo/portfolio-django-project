from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from presentation.models import *

def accueil(request):

    template = loader.get_template('index.html')
    context = {
        "title":"homepage",
    }

    return HttpResponse(template.render(context,request))

def contact(request):


    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'fullname':fullname,
            'email':email,
            'subject':subject,
            'message':message
        }

        message = '''
        New message : {}

        From: {}

        '''.format(data['message'],data['email'])

        send_mail(data['subject'],message,'',['onjatiana.ramanitrarivo@gmail.com'])



    template = loader.get_template('contact.html')
    context = {
        "title":"contact",
    }

    return HttpResponse(template.render(context,request))


def observation(request):

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        observation = request.POST.get('observation')

        if ObservationModel.objects.create(fullname=fullname,email=email,observation=observation):
            print('insertion réussi')
       
    
    template = loader.get_template('observation.html')
    context = {
        "title":"observation",
    }

    return HttpResponse(template.render(context,request))