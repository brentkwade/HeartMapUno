from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'dashboard/dashboard.html')

def user(request):
    return render(request, 'dashboard/user.html')