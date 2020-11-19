from rest_framework import serializers
from .models import *

class QuestaoSerializer(serializers.ModelSerializer):
	class Meta:
		model= Questao
		fields= ['id', 'texto', 'imagem', 'alternativa_correta', 'ano', "user_id"]

	# def clean_ano(self, *args, **kwargs):
	# 	ano = self.cleaned_data.get('ano')
	# 	current_year = datetime.now().year
	# 	if not (ano >= 2002 and ano <= current_year):
	# 		raise forms.ValidationError("O ano deve estar entre 2002 e " + str(current_year))
	# 	return ano