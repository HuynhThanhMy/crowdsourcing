from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home_screen_view(request):
    print(request.headers)
    return render(request, "base.html", {})
