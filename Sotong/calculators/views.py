from django.shortcuts import render

# Create your views here.
def calc_view(request):
    
    return render(request, 'calc/calc-page.html')

def result_view(request):
    return render(request, 'calc/calc-res-page.html')