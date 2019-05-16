from django import forms

from .models import Scan


class HeartRate(forms.ModelForm):
    class Meta:
        model = Scan
        fields = ('title','csv')