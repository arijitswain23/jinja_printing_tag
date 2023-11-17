from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This is our assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)

def login(request):
    d={'username':'Arijit'}
    return render(request,'login.html',context=d)