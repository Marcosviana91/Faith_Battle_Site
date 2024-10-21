from django.forms import ModelForm
from .models import Enquetes, Artigo


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


class FormArtigos(ModelForm):
    class Meta:
        model = Artigo
        # fields = '__all__'
        fields = ['titulo', 'img_capa','conteudo']
        # exclude = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
        self.fields['titulo'].widget.attrs.update({'id':'novo_conteudo_titulo'})
        self.fields['conteudo'].widget.attrs.update({'id':'novo_conteudo'})
