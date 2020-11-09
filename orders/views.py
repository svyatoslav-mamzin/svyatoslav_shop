from django.http import HttpResponse
from django.shortcuts import render
from .tasks import order_created

def order_create(request):
    order_created.delay()
    return HttpResponse('Oki-doki')
