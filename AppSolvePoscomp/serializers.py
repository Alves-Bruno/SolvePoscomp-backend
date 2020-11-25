from rest_framework import serializers
from .models import *
from datetime import datetime

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['nome', 'id']

class TagSerializerNome(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['nome']
		
# class QuestaoSerializer(serializers.ModelSerializer):
	
# 	tags = serializers.ReadOnlyField()
# 	created_at = serializers.ReadOnlyField()
# 	updated_at = serializers.ReadOnlyField()

# 	class Meta:
# 		model= Questao
# 		fields= ['id', 'texto', 'imagem', 'alternativa_correta', 'ano', "tags", 'created_at', 'updated_at', 'user_id']
# 		extra_kwargs = {'imagem': {'required': False, 'allow_null': True}}

# 	def validate_ano(self, submitted_year):
# 		# ano = self.cleaned_data.get('ano')
# 		current_year = datetime.now().year
# 		if not (submitted_year >= 2002 and submitted_year <= current_year):
# 			raise serializers.ValidationError("O ano deve estar entre 2002-" + str(current_year)+ ".")
# 		return submitted_year
	
# 	def validate_alternativa_correta(self, submitted_alternativa):
# 		# Test if the submitted value is a char:
# 		if not submitted_alternativa.isalpha():
# 			raise serializers.ValidationError("A alternativa deve ser um caractere entre A-E.")
# 		upper_alternativa = submitted_alternativa.upper()
# 		if not (upper_alternativa >= "A" and upper_alternativa <= "E"):
# 			raise serializers.ValidationError("A alternativa deve ser um caractere entre A-E.")
# 		return submitted_alternativa.upper()
	
# 	def validate_add_tags(self, list_of_tags):
# 		# print(list_of_tags)
# 		return list_of_tags


class CadernoSerializer(serializers.ModelSerializer):
	
	questoes = serializers.ReadOnlyField()
	id = serializers.ReadOnlyField()
	# criador_id = serializers.ReadOnlyField()
	
	class Meta:
		model = Caderno
		fields = ['id', 'nome', 'descricao', 'criador_id', 'questoes']

	def validate(self, data):
		
		# Usuario nao pode cadastrar dois cadernos com o mesmo nome
		print(data)
		query = Caderno.objects.filter(criador_id=data['criador_id'], nome=data['nome'])
		if len(query) == 0:
			return data
		else:
			raise serializers.ValidationError("Usuario ja possui um caderno com esse nome.")

class CadernoSerializerPut(serializers.ModelSerializer):
	
	# questoes = serializers.ReadOnlyField()
	# id = serializers.ReadOnlyField()
	# criador_id = serializers.ReadOnlyField()
	
	class Meta:
		model = Caderno
		fields = ['nome', 'descricao']
		extra_kwargs = {'nome': {'required': False}, 'descricao': {'required':False}}
