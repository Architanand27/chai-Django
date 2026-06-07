from django.shortcuts import render

# Create your views here.
def arc_home(request):
    return render(request, 'arc/newArc.html')
