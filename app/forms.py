from django import forms
from app.models.cm_license import CmLicense

class CmLicenseForm(forms.ModelForm):
    """
    Form for creating and updating CM licenses.
    """
    class Meta:
        model = CmLicense
        fields = ['account_id', 'profile_id', 'report_id']
        widgets = {
            'account_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'report_id': forms.NumberInput(attrs={'class': 'form-control'}),
        }
