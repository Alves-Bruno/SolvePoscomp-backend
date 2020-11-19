from rest_framework import serializers
from .models import *
from datetime import datetime

class QuestaoSerializer(serializers.ModelSerializer):
	class Meta:
		model= Questao
		fields= ['id', 'texto', 'imagem', 'alternativa_correta', 'ano', "user_id"]
		extra_kwargs = {'imagem': {'required': False, 'allow_null': True}}

	def validate_ano(self, submitted_year):
		# ano = self.cleaned_data.get('ano')
		current_year = datetime.now().year
		if not (submitted_year >= 2002 and submitted_year <= current_year):
			raise serializers.ValidationError("O ano deve estar entre 2002-" + str(current_year)+ ".")
		return submitted_year
	
	def validate_alternativa_correta(self, submitted_alternativa):
		# Test if the submitted value is a char:
		if not submitted_alternativa.isalpha():
			raise serializers.ValidationError("A alternativa deve ser um caractere entre A-E.")
		upper_alternativa = submitted_alternativa.upper()
		if not (upper_alternativa >= "A" and upper_alternativa <= "E"):
			raise serializers.ValidationError("A alternativa deve ser um caractere entre A-E.")
		return submitted_alternativa.upper()

class QuestaoSerializerGet(serializers.ModelSerializer):
	class Meta:
		model= Questao
		fields= ['id', 'texto', 'imagem', 'alternativa_correta', 'ano', "user_id", "created_at", "updated_at", "texto_imagem"]