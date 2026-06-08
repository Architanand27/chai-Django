from django.shortcuts import render
from .models import chaiVarity, store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def arc_home(request):
    chais=chaiVarity.objects.all()
    return render(request, 'arc/newArc.html', {'chais': chais})


def chai_details(request, chai_id):
    chai= get_object_or_404(chaiVarity,pk=chai_id)
    return render(request, 'arc/chai_details.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method== 'POST':
        form= ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety=form.cleaned_data['chai_variety']
            stores = store.objects.filter(chai_varieties=chai_variety)
    else:
        form=ChaiVarietyForm()

    return render(request, 'arc/chai_stores.html',{'stores': stores, 'form':form})