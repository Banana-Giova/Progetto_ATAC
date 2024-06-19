from django.shortcuts import render
import django.http
from django.views import View

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self,request):
        return render(request, "home.html")

