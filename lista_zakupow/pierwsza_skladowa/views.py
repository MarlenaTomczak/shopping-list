from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def str_glowna(request,*args,**kwargs):
	kontekst= {
	"numer":"1111111111",
	"mail": "1ffff@ww.com",
	"lista": [1,2,3,4]
	}
	return render(request,"strona_glowna.html",kontekst)

def tworzenie_listy(request,*args,**kwargs):
	return render(request,"lista.html",{})

def zpara(request, napis, *args,**kwargs):
	return HttpResponse(f"<h1> {napis} </h1>")