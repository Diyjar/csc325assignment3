from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1><p>This is the about page.</p>")

@api_view(["GET"])
def api_status(request):
    return Response({"status": "ok", "message": "CSC325 API is running"})

@api_view(["GET"])
def api_health(request):
    return Response({"healthy": True})