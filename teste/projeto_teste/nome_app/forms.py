from django import forms
from .models import Aluno, Frequencia

class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['aluno', 'presente']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aluno'].queryset = Aluno.objects.all()
