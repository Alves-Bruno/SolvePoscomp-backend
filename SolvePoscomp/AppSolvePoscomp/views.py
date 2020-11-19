from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


# Create your views here.
# from django.http import HttpResponse
# from .forms import QuestaoForm
from .models import Questao
from django.contrib.auth.models import User
# from django.http import JsonResponse

# REST
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import QuestaoSerializer, QuestaoSerializerGet

def index(request):
    return render(request, 'home.html', {'user': request.user.username})
    # return HttpResponse("POSCOMP APP - WELCOME " + str(request.user.username) + "!" + "{{% csrf_token %}}")

## QUESTAO VIEWS
@csrf_exempt
def questao_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        questoes = Questao.objects.all()
        serializer = QuestaoSerializerGet(questoes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            data = JSONParser().parse(request)
            serializer = QuestaoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({'Error':"User not logged in."},status=401)

@csrf_exempt
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
        serializer = QuestaoSerializerGet(questao)
        return JsonResponse(serializer.data)
    
    # @login_required
    if request.user.is_authenticated:
        # Checking if the question belongs to the user
        if questao.user_id.id == request.user.id:
            if request.method == 'PUT':
                data = JSONParser().parse(request)
                # data = data + {"user_id":request.user}
                data["user_id"] = request.user.id 
                # print(data)
                serializer = QuestaoSerializer(questao, data=data)

                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                    
                return JsonResponse(serializer.errors, status=400)

            elif request.method == 'DELETE':
                questao.delete()
                return HttpResponse(status=204)
        else:
            return JsonResponse({'Error':"Questão pertence a outro usuário"},status=401)