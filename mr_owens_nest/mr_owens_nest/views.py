from django.shortcuts import render

def home(request):
    heading = 'Mr Owen\'s Nest'
    context = {
        'heading': heading,
    }
    return render(request, 'home.html', context=context)

def fake(request):
    heading = 'Trownsmen'
    context = {
        'heading': heading,
    }
    return render(request, 'fake.html', context=context)