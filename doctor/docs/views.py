from django.shortcuts import render
from docs.models import Doctor


def index(request):
    doc = Doctor()
    cursor = doc.listado()
    contexto = {
        'lista_docs': cursor
        }
    return render(request, 'listado_docs.html', contexto)
def search(request):
    doc = Doctor()
    cursor = doc.listado()
    contexto = {
        'lista_docs': cursor
        }
    return render(request, 'search_docs.html', contexto)

# Create your views here.
