from django.shortcuts import render
from .models import Tag

def main_page(request):
    tags = Tag.objects.all()
    return render(request, 'main_page.html', {'tags': tags})