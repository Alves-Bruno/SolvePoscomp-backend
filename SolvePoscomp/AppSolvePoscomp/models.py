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
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

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

class QuestaoTags(models.Model):
	questao_id = models.ForeignKey('Questao', on_delete=models.CASCADE)
	tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)

