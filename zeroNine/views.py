from django.shortcuts import render

# Create your views here.
def lists(request):
    return render(request, 'zeroNine/list.html', {})
