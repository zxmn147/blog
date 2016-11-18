from django.shortcuts import render


from book.models import Book


def book(request):
    '''
    Render the article page
    '''
    context = {'books':Book.objects.all()}
    return render(request, 'book/book.html', context)
