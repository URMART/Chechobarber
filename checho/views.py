from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.
#return HttpResponseRedirect(reverse('territorio:aprendiz'))
def index(request):

    return render(request, 'index.html')