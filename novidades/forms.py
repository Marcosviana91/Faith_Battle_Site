from django.forms import ModelForm
from .models import Enquetes


class FormEnquetes(ModelForm):
    class Meta:
        model = Enquetes
        # fields = '__all__'
        fields = ['titulo', 'descricao']
        # exclude = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
