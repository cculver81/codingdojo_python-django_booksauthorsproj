from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This is a test of the books_authors_proj setup.')
