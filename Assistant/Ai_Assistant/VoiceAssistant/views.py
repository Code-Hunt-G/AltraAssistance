from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def HomePage(request):
    return render(request, 'voiceAssist.html')

def handle_hello(request):
    if request.method == "POST":
        # Perform your Python logic here
        response_message = "Python function called successfully!"
        return JsonResponse({"message": response_message})
    return JsonResponse({"error": "Invalid request method"}, status=400)
