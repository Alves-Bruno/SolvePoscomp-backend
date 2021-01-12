# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# from .serializers import *
from rest_framework import serializers
from datetime import datetime


class Questao(models.Model):
	# id = automagically_created
	texto = models.CharField(max_length=10000)
	alt_A = models.CharField(max_length=1000)
	alt_B = models.CharField(max_length=1000)
	alt_C = models.CharField(max_length=1000)
	alt_D = models.CharField(max_length=1000)
	alt_E = models.CharField(max_length=1000)
	imagem = models.ImageField(blank=True)
	alternativa_correta = models.CharField(max_length=1)
	ano = models.IntegerField()
	texto_imagem = models.CharField(max_length=10000, blank=True)
	user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def tags(self):
		all_tags = QuestaoTags.objects.filter(questao_id=self.id)
		dict_tags_list = []
		for tag in all_tags:
			tag_nome = (Tag.objects.get(id=tag.tag_id.id)).nome
			dict_tags_list.append({'id':tag.tag_id.id, 'nome':tag_nome})
		return dict_tags_list
	
	def delete_tags(self):
		tags = QuestaoTags.objects.filter(questao_id=self)
		for tag in tags:
			tag.delete()
		
	def add_tags(self, list_of_tags):
		# Delete all tags 
		self.delete_tags()

		for tag_name in list_of_tags:
			tag_in_db = Tag.objects.filter(nome=tag_name)
			# Tag already exists:
			if len(tag_in_db) > 0:
				# tag_in_db[0].save()
				new_questaotags = QuestaoTags(questao_id=self, tag_id=tag_in_db[0])
				new_questaotags.save()
			# Tag do not exists:
			else:
				new_tag = Tag(nome=tag_name)
				new_tag.save()
				new_questaotags = QuestaoTags(questao_id=self, tag_id=new_tag)
				new_questaotags.save()


class Solucao(models.Model):
	# id = automagically_created
	questao_id = models.ForeignKey('Questao', on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	texto = models.CharField(max_length=1000)
	imagem = models.ImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)	

class RelacaoCadernoQuestao(models.Model):
	caderno_id = models.ForeignKey('Caderno', on_delete=models.CASCADE)
	questao_id = models.ForeignKey('Questao', on_delete=models.CASCADE)

class Simulado(models.Model):
	caderno_id = models.ForeignKey('Caderno', on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class QuestaoSimulado(models.Model):
	questao_id = models.ForeignKey('Questao', on_delete=models.CASCADE)
	alternativa_selecionada = models.CharField(max_length=1, default='#')
	simulado_id = models.ForeignKey('Simulado', on_delete=models.CASCADE)

class Tag(models.Model):
	nome = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return str({'id': self.id, 'nome': self.nome})

class QuestaoTags(models.Model):
	questao_id = models.ForeignKey('Questao', on_delete=models.CASCADE, default=1)
	tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE, default=1)

	def __str__(self):
		return str({'id': self.id, 'questao_id': self.questao_id, "tag_id":self.tag_id})

class QuestaoSerializer(serializers.ModelSerializer):
	
	tags = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	id = serializers.ReadOnlyField()

	# alt_A = serializers.ReadOnlyField()
	# alt_B = serializers.ReadOnlyField()
	# alt_C = serializers.ReadOnlyField()
	# alt_D = serializers.ReadOnlyField()
	# alt_E = serializers.ReadOnlyField()
	
	class Meta:
		model= Questao
		fields= ['id', 'texto', 'alt_A', 'alt_B', 'alt_C', 'alt_D', 'alt_E', 'imagem', 'alternativa_correta', 'ano', "tags", 'created_at', 'updated_at', 'user_id']
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
	
	def validate_add_tags(self, list_of_tags):
		# print(list_of_tags)
		return list_of_tags

class Caderno(models.Model):
	nome = models.CharField(max_length=100)
	descricao = models.CharField(max_length=300, default='')
	criador_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

	def questoes(self):
		all_questoes = RelacaoCadernoQuestao.objects.filter(caderno_id=self.id)
		dict_questoes_list = []
		num_of_questoes = 1
		for questao in all_questoes:
			serializer = QuestaoSerializer(Questao.objects.get(id=questao.questao_id.id))
			dict_questoes_list.append(serializer.data)
			num_of_questoes = num_of_questoes + 1

		return dict_questoes_list	

	def add_questao(self, questao_id):
		# q = Questao.objects.get(id=questao_id)
		# Testa se a questao existe:
		query = Questao.objects.filter(id=questao_id)
		if len(query) == 1:
			add_RelacaoCadernoQuestao = RelacaoCadernoQuestao(questao_id=questao_id, caderno_id=self.id)
			add_RelacaoCadernoQuestao.save()
			return True
		else:
			return False

	def remove_questao(self, questao_id):
		query = RelacaoCadernoQuestao.objects.filter(questao_id=questao_id, caderno_id=self.id)
		# Testa se a questao ja vinculada ao caderno
		if len(query) == 1:
			delete(query[0])
			return True
		# Se nao esta vinculada, somente retorna
		else:
			return False