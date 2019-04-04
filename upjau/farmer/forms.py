from django import forms
from .models import *

class FarmLandForm(forms.ModelForm):
    class Meta:
        model = farmer_farmLand
        fields = ['address', 'state', 'district', 'subDistrict', 'pincode', 'size', 'soilType', 'waterSystem', 'purpose', 'server']
