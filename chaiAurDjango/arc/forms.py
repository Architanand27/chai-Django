from django import forms
from .models import chaiVarity

class ChaiVarietyForm(forms.Form):
    chai_variety=forms.ModelChoiceField(queryset=chaiVarity.objects.all(),label= "select chai variety")

