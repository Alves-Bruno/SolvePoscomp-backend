from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Questao)
admin.site.register(Solucao)
admin.site.register(Simulado)
admin.site.register(Caderno)
admin.site.register(RelacaoCadernoQuestao)
admin.site.register(QuestaoSimulado)
admin.site.register(Tag)
admin.site.register(QuestaoTags)

