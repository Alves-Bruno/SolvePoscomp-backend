# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Questao(models.Model):
	# id = automagically_created
	texto = models.CharField(max_length=1000)
	imagem = models.ImageField(blank=True)
	alternativa_correta = models.CharField(max_length=1)
	ano = models.IntegerField()
	texto_imagem = models.CharField(max_length=1000, blank=True)
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

class Caderno(models.Model):
	nome = models.CharField(max_length=30, unique=True)
	criador_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

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
	nome = models.CharField(max_length=30, unique=True)
	def __str__(self):
		return str({'id': self.id, 'nome': self.nome})

class QuestaoTags(models.Model):
	questao_id = models.ForeignKey('Questao', on_delete=models.CASCADE, default=1)
	tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE, default=1)

	def __str__(self):
		return str({'id': self.id, 'questao_id': self.questao_id, "tag_id":self.tag_id})

