from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import time


def send_email(request):
    send_email.delay()
    return HttpResponse("<h1>Done Sending</h1>")


def test(request):
    response = requests.get(
        "https://e9d281d2-ddac-4cb5-be91-418470426aac.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())
