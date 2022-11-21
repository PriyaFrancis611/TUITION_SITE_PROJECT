from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
def registration(request):
    return render(request,'registration.html')
def admindashboard(request):
    return render(request,'admin-dashboard/index.html')

