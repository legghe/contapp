from django.shortcuts import render
from django.http import HttpResponse
from .models import Counter, WebPageTxt


def index(request):
    q = Counter.objects.get(nome="contaVisite")
    q.openedpage = q.openedpage + 1
    q.save()

    txt = WebPageTxt.objects.get(pk=1)
    return render(request, 'index.html', {'testo': txt})
    #return HttpResponse(txt + str(q.openedpage))
