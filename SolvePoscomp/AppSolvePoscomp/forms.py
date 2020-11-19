from django.forms import ModelForm, forms
from .models import Questao
from datetime import datetime


class QuestaoForm(ModelForm):
	class Meta:
		model= Questao
		fields= ['texto', 'imagem', 'alternativa_correta', 'ano', "user_id"]

	def clean_ano(self, *args, **kwargs):
		ano = self.cleaned_data.get('ano')
		current_year = datetime.now().year
		if not (ano >= 2002 and ano <= current_year):
			raise forms.ValidationError("O ano deve estar entre 2002 e " + str(current_year))
		return ano