
from django.shortcuts import render, redirect
from .models import Flan, ContactForm, Testimonio
from .forms import ContactFormForm, TestimonioForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(req):
    public_flans = Flan.objects.filter(is_private=False)
    return render(req, 'index.html', {'public_flans': public_flans})

def about(req):
    return render(req, 'about.html')

@login_required
def welcome(req):
    private_flans = Flan.objects.filter(is_private=True)
    return render(req, 'welcome.html',{'private_flans': private_flans})

def contact(req):
    if req.method == 'POST':
        form = ContactFormForm(req.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return redirect('success') 

    else:
        form = ContactFormForm()
    return render(req, 'contact.html', {'form': form})

def success(req):
    return render(req, 'success.html', {})

def testimonio(request):
    testimonios = Testimonio.objects.all().order_by('-created_at')
    return render(request, 'testimonio.html', {'testimonio': testimonios})

def crear_testimonio(request):
    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonio')  # Redirige a la página de testimonios después de crear
    else:
        form = TestimonioForm()
    return render(request, 'crear_testimonio.html', {'form': form})
