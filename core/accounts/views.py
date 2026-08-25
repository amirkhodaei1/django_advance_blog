from django.shortcuts import render
from django.http import HttpResponse
import time
def send_email(request):
    send_email.delay()
    return HttpResponse("<h1>Done Sending</h1>")