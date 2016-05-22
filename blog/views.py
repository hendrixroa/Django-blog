from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import loader
from blog.models import *

# Create your views here.

def main(request):
    entrada = Entrada.objects.all().order_by("-fecha")
    paginator = Paginator(entrada,4)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: Pagina = 1

    try:
        entrada = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        entrada = paginator.page(paginator.num_pages)

    context = {'entrada': entrada}    
    return render(request,'blog/listado.html',context)
