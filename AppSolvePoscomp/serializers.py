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

		
class QuestaoSerializer(serializers.ModelSerializer):
	
	tags = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	# user_id = serializers.ReadOnlyField()
	# texto_imagem
	# insert_tags = TagSerializerNome(many=True) 
	
	# serializers.ListField( 
	# 	many=True,
    # 	child = serializers.CharField() 
    # ) 

	class Meta:
		model= Questao
		fields= ['id', 'texto', 'imagem', 'alternativa_correta', 'ano', "tags", 'created_at', 'updated_at', 'user_id']
		extra_kwargs = {'imagem': {'required': False, 'allow_null': True}}
		# tags = serializers.ListField(
		# 	child=TagSerializer())

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
	
	def validate_add_tags(self, list_of_tags):
		# print(list_of_tags)
		return list_of_tags

	# def create(self, validated_data):
	# 	# print(validated_data)
	# 	q = Questao(texto=validated_data['texto'], 
	# 				imagem=validated_data['imagem'],
	# 				alternativa_correta=validated_data['alternativa_correta'],
	# 				ano=validated_data['ano'],
	# 				user_id=validated_data['user_id'])
	# 	q.save()
	# 	q.add_tags(validated_data['add_tags'])
	# 	# return Questao.objects.get(id=1)
	# 	return q

