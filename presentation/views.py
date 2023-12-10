from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail

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

        send_mail(data['subject'],message,'',['rama14jill@gmail.com'])



    template = loader.get_template('contact.html')
    context = {
        "title":"contact",
    }

    return HttpResponse(template.render(context,request))