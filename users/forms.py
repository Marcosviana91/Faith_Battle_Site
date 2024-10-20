from django import forms

class UploadFileForm(forms.Form):
    imagem = forms.ImageField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     print(field)
        self.fields['imagem'].widget.attrs.update({'class':'form-control'})
        self.fields['imagem'].label = 'Enviar Imagem'