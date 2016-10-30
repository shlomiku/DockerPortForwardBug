import json
from django.http import HttpResponse

def list(request):
    return HttpResponse(json.dumps(["second ", "list "]))

