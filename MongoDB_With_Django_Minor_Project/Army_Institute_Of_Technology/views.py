from django.shortcuts import render, HttpResponse
from .forms import Contact_us_form
# Create your views here.
def Contact_us(request):
    if request.method=='GET':
        form= Contact_us_form
        return render(request, 'Contact_us.html', {'form': form, })
    if request.method== 'POST':
        form= Contact_us_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Submitted')
def home(request):
    return render(request, 'home.html',)
def About_us(request):
    return render(request, 'About_us.html',)

