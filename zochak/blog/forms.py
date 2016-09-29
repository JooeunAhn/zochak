from django import forms
from .models import Zocbo

class ZocboForm(forms.ModelForm):
    class Meta:
        model = Zocbo
        fields = ["name", "subject", "content", "file",]
