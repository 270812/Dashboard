from django.shortcuts import render
from django.http import HttpResponse
from .models import contactdata
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def index(request):
    return render(request, 'dashboard.html')

def users(request):
    data = contactdata.objects.all()
    # print(data)
    return render(request, 'user.html', {'data':data})




# def users(request):
#     data = contactdata.objects.all()
#     print(data)
#     return render(request, 'user.html', {'data':data} )


 


# def project(request):
#       if request.method == "POST":
#         name = request.POST['name']
#         position = request.POST['position']
#         country = request.POST['country']
#         portfolio = request.POST['portfolio']
#         role = request.POST['role']
#         data = contactdata.objects.create(name=name, position=position, country=country, portfolio=portfolio, role=role)
#       return render(request, 'user.html')





     
def addDatas(request):
    if request.method == "POST":
        name = request.POST['name']
        position = request.POST['position']
        country = request.POST['country']
        portfolio = request.POST['portfolio']
        role = request.POST['role']
        image = request.FILES.get('image')
        data = contactdata.objects.create( image=image ,name=name, position=position, country=country, portfolio=portfolio, role=role)
        data.save()
        print(data)
        # return render(request, 'user.html')    
   
    return render(request, 'add.html')


def edit(request, id):
    form = get_object_or_404(contactdata, id=id)
    if request.method == "POST":
        form.name = request.POST.get('name')
        form.position = request.POST.get('position')
        form.country = request.POST.get('country')
        form.portfolio = request.POST.get('portfolio')
        form.role = request.POST.get('role')
        form.image = request.FILES.get('image')
        form.save()
        return redirect('userpage')
    return render(request, 'edit.html',{'form':form})

# def delete(request, pk):
#     form = get_object_or_404(contactdata, id=id)
#     form.delete()
#     return redirect('user.html')

def delete(request, id):
    form = get_object_or_404(contactdata, id=id)
    form.delete()
    return redirect('userpage')





    












