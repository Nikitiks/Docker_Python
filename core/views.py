from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import json
import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


path = '/project/static/books/books.json'

@csrf_exempt
def add_book(request):
    if request.method == "POST":
            
        data = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'status': request.POST['status']
        } 

        books = read_books()
        books.append(data)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(books, file, indent=2, ensure_ascii=False)

        return JsonResponse({'status':'saved'})
    
    return JsonResponse({'status':'This address only accepts post'})

def get_books(request):
    books = read_books()
    return JsonResponse({'books':books})


def read_books():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []
    
