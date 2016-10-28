from django.shortcuts import render
import datetime
from django.core.paginator import Page
def main(request):
    '''
    Render the main page
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很棒','now':now}
    return render(request, 'main/main.html', context)
def about(request):
    '''
    Render the about Page
    '''
    return render(request, 'main/about.html')

def contact(request):
    '''
    Render the contact Page
    '''
    return render(request, 'main/contact.html')