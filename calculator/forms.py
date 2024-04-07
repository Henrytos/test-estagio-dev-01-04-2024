from django import forms

class FormCalculate(forms.Form):
    rate_one = forms.FloatField(label='Taxa do 1-Mês', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '12.000,00'}), required=True)
    rate_two = forms.FloatField(label='Taxa do 2-Mês', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '12.000,00'}), required=True)
    rate_three = forms.FloatField(label='Taxa do 3-Mês', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '12.000,00'}), required=True)
    
    rate_value = forms.FloatField(label='Valor da tarifa', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0,3'}), required=True)
    
    RATE_CHOICES = [
        ('Comercial', 'Comercial'),
        ('Residencial', 'Residencial'),
        ('Industrial', 'Industrial'),
    ]
    rate_type = forms.ChoiceField(label='Tipo de tarifa', choices=RATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
