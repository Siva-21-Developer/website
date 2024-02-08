from django import forms


class Form_input(forms.Form):
    Form_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Form_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))