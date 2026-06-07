from django.shortcuts import render
from .models import chaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def arc_home(request):
    chais=chaiVarity.objects.all()
    return render(request, 'arc/newArc.html', {'chais': chais})


def chai_details(request, chai_id):
    chai= get_object_or_404(chaiVarity,pk=chai_id)
    return render(request, 'arc/chai_details.html', {'chai': chai})