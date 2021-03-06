# Generated by Django 3.1.3 on 2020-12-01 13:01

from django.db import migrations
from django.core.files import File
from pathlib import Path
from django.conf import settings
import re

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

def split_alternatives(texto):
	
	# Procura por cada alternativa: [A-E]) Texto ...
	pattern = re.compile(r'\n[A-Ea-e]\).*')
	matches = pattern.finditer(texto)

	splited_alternatives = []
	questao_end = 0

	first = True
	for alternative in matches:

		if first == True:
			questao_end = alternative.start()
			first = False

		alternative_without_breakline = alternative.group(0).replace('\n', '')
		
		# Remove somente o texto da alternativa.
		inline_regex = re.findall(r'\w.*', alternative_without_breakline[2:])
		splited_alternatives.append(inline_regex[0])
	
	return texto[:questao_end], splited_alternatives


def add_questoes_2019(apps, schema_editor):

    Questao = apps.get_model('AppSolvePoscomp', 'Questao')
    User = apps.get_model(settings.AUTH_USER_MODEL)
    # Tag = apps.get_model('AppSolvePoscomp', 'Tag')
    # QuestaoTags = apps.get_model('AppSolvePoscomp', 'QuestaoTags')

    user = User.objects.get(username='PoscompTeam')

    info_file = open(str(BASE_DIR) + '/QUESTOES/2019/INFO-2019.txt', 'r')
    file_line_list = info_file.read().split('\n')
    for line in file_line_list:
        question_info = line.split('_')

        if len(question_info) == 3:
            print(question_info)
            q_num = int(question_info[0])
            alternativa_correta=question_info[1]

            texto = open(str(BASE_DIR) + '/QUESTOES/2019/POSCOMP_2019_QUESTAO-'+str(q_num)+'.txt')
            questao_texto, questao_alternativas = split_alternatives(texto.read())

            imagem = File(open(str(BASE_DIR) + '/QUESTOES/2019/POSCOMP_2019_QUESTAO-'+str(q_num)+'.png', 'rb'))
            questao = Questao(  texto=questao_texto,
                                alt_A = questao_alternativas[0],
                                alt_B = questao_alternativas[1],
                                alt_C = questao_alternativas[2],
                                alt_D = questao_alternativas[3],
                                alt_E = questao_alternativas[4],
                                ano=2019,
                                alternativa_correta=alternativa_correta,
                                user_id=user,
                                )

            questao.imagem.save('QUESTAO-2019-' + str(q_num) + '.png', imagem)
        

def rm_questoes_2019(apps, schema_editor):
    Questao = apps.get_model('AppSolvePoscomp', 'Questao')
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User.objects.get(username='PoscompTeam')

    list_questao = Questao.objects.filter(ano=2019, user_id=user)

    for questao in list_questao:
        questao.delete()



class Migration(migrations.Migration):

    dependencies = [
        ('AppSolvePoscomp', '0010_auto_20210112_1604'),
    ]

    operations = [
        migrations.RunPython(add_questoes_2019, rm_questoes_2019),
    ]
