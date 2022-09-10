from django.shortcuts import render

# Create your views here.
def hello(request, name):
    data = {'msg': 'Olá, ', 'name': name}
    return render(request, 'helloWorldApp/hello.html', data)