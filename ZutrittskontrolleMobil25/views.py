from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess

@csrf_exempt
def shutdown_view(request):
    if request.META.get("REMOTE_ADDR") != "127.0.0.1":
        return HttpResponse("Access denied", status=403)
    if request.method == "POST":
        # This will shut down the system
        subprocess.call(['sudo', 'shutdown', '-h', 'now'])
        return HttpResponse("System is shutting down...")
    return HttpResponse("Method not allowed", status=405)