from django.http import HttpResponse
from django.template import loader


def index(request):
    tem = loader.get_template("bootstrap.html").render(request=request)
    return HttpResponse(tem)