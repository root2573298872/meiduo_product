import re

from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        pass