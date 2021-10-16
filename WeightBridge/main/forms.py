from django import forms
from .models import Reading


class FirstReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields=['weight1', 'vehicleNumber', 'vehicleType']

class SecondReading(forms.ModelForm):
    class Meta:
        model = Reading
        fields=['weight2']