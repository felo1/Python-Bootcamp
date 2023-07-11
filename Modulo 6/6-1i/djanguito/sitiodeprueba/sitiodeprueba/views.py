from django.http import HttpResponse

def index(request):
    returnHttpResponse("<h1>Hola amigos</h1>")

