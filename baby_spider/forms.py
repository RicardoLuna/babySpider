from django import forms

from .models import Spider

class SpiderForm(forms.ModelForm):
    
    class Meta:
        model = Spider
        fields = (
            'url', 'metodo', 'consulta', 'consulta_url', 'consulta_metodo',
            'consulta_step2', 'author', 'campo1', 'campo2', 'campo3' , 
            'campo4', 'campo5'
        )