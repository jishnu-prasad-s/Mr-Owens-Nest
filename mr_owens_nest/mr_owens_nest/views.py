from django.shortcuts import render

def home(request):
    heading = 'Mr Owen\'s Nest'
    context = {
        'heading': heading,
    }
    return render(request, 'home.html', context=context)