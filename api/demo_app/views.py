from django.shortcuts import render

# Create your views here.
def hello_user(request):
    return render(request, './templates/member.html')