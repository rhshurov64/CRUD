from django.shortcuts import render,HttpResponseRedirect, redirect
from .forms import AddForm
from .models import AddUser

# Create your views here.


# Add and Show 
def home(request):
    if request.method == 'POST':
        fm = AddForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ag = fm.cleaned_data['age']
            rg = AddUser(name=nm,email=em,age=ag)
            rg.save()
            fm = AddForm()
    else:
        fm = AddForm()
    list = AddUser.objects.all()
    return render(request, 'main/show.html', {'form':fm, "li":list})

# Delete
def delete_data(request,id):
    if request.method =='POST':
        pi = AddUser.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

# Views for Update
def update_data(request,id):
    if request.method =='POST':
        pi = AddUser.objects.get(pk=id)
        fm = AddForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = AddUser.objects.get(pk=id)
        fm = AddForm(instance=pi)
        
    return render(request,'main/update.html',{'form':fm})
