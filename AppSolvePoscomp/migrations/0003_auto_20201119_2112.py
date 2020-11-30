# Generated by Django 3.1.3 on 2020-11-19 21:12

from django.db import migrations

def add_basic_tags(apps, schema_editor):

    basic_tags = ['Matemática', 'Fundamentos da Computação', 'Tecnologia da Computação',

        'Álgebra Linear',
        'Análise Combinatória',
        'Cálculo Diferencial e Integral',
        'Geometria Analítica',
        'Lógica Matemática',
        'Matemática Discreta',
        'Probabilidade',
        'Estatística',

        'Análise de Algoritmos',
        'Algoritmos e Estrutura de Dados',
        'Arquitetura e Organização de Computadores',
        'Circuitos Digitais',
        'Linguagens de Programação',
        'Linguagens Formais, Autômatos e Computabilidade',
        'Organização de Arquivos e Dados',
        'Sistemas Operacionais',
        'Técnicas de Programação',
        'Teoria dos Grafos',

        'Banco de Dados',
        'Compiladores',
        'Computação Gráfica',
        'Engenharia de Software',
        'Inteligência Artificial',
        'Processamento de Imagens',
        'Redes de Computadores',
        'Sistemas Distribuídos']


    Tag = apps.get_model('AppSolvePoscomp', 'Tag')
    for tag in basic_tags:
        # if len(tag) <= 30:
        new_tag = Tag(nome=tag)
        new_tag.save()

class Migration(migrations.Migration):

    dependencies = [
        ('AppSolvePoscomp', '0002_questao_user_id'),
    ]

    operations = [
        migrations.RunPython(add_basic_tags),
    ]
