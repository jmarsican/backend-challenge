import json

from django.http import HttpRequest, HttpResponse


def usage(request: HttpRequest) -> HttpResponse:
    # implement your code here to retrieve the data that was stored in the database
    # using the DataInitialiser and return it in JSON format

    return HttpResponse(json.dumps([]))
