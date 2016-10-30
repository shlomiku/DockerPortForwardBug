import json
from django.http import HttpResponse

def list(request):
    return HttpResponse(json.dumps(["hello ", "this ", "is ", "a message"]))

