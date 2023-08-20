from django import forms

class AdvertisementForm(forms.Form):
    title =         forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
    description =   forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control-lg'})) #многострочное поле
    price =         forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control-lg'}))
    is_auction =    forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control-lg'})) #этот параметр стал необязателным
    image =         forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-lg'}))
