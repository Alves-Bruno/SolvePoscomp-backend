from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


# Create your views here.
# from django.http import HttpResponse
from .forms import QuestaoForm
from .models import Questao
from django.contrib.auth.models import User
# from django.http import JsonResponse

# REST
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import QuestaoSerializer

def index(request):
    return HttpResponse("POSCOMP APP - WELCOME " + str(request.user.username) + "!")

@login_required(redirect_field_name='/accounts/login')
def questao_create(request):
	# new_questao = 0
	# user_instance = User.objects.get(username=request.user.username)
	print(request.user)
	initial_values = {
		"user_id": request.user
	}
	
	form = QuestaoForm(request.POST or None, initial=initial_values)
	if form.is_valid():
		data = form.cleaned_data
		new_questao = form.save()
		return JsonResponse(data)
	else:
		data = form.errors.as_json()
		return JsonResponse(data, status=400) 

def questao_by_id(request, questao_id):
	questao = get_object_or_404(Questao, id=questao_id)
	return render(request, 'questao_by_id.html', {'questao': questao})

# def account_confirm_email(request, uidb64, token):
# 	print(uidb64)
# 	print(token)
# 	return HttpResponse('')

## QUESTAO VIEWS
@csrf_exempt
def questao_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        questoes = Questao.objects.all()
        serializer = QuestaoSerializer(questoes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestaoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@login_required(redirect_field_name='/')
def questao_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    print(request.user)


    try:
        questao = Questao.objects.get(id=pk)
    except Questao.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestaoSerializer(questao)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestaoSerializer(questao, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        questao.delete()
        return HttpResponse(status=204)