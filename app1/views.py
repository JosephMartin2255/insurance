from django.shortcuts import render

# Create your views here.

def loginpage(request):
    return render(request, 'loginpage.html')
def adminhome(request):
    return render(request, 'adminhome.html')
def logout(request):
    return render(request,'loginpage.html')