from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def accueil(request):

    template = loader.get_template('index.html')
    context = {
        "title":"homepage",
    }

    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template('contact.html')
    context = {
        "title":"contact",
    }

    return HttpResponse(template.render(context,request))