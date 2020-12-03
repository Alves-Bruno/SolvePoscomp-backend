from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


# Create your views here.
# from django.http import HttpResponse
# from .forms import QuestaoForm
from .models import *
from django.contrib.auth.models import User
# from django.http import JsonResponse

# REST
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt
from django.conf import settings

import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions
from django.contrib.auth.models import AnonymousUser

def get_user_by_token(request):
    if "Authorization" not in request.headers:
        return AnonymousUser(), 'Authorization Header required.'

    auth_header = request.headers["Authorization"]
    _, token = auth_header.split(' ')
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
    except jwt.DecodeError as identifier:
        # raise exceptions.AuthenticationFailed('Your token is invalid,login')
        return AnonymousUser(), 'JWT Token is invalid.'
    except jwt.ExpiredSignatureError as identifier:
        # raise exceptions.AuthenticationFailed('Your token is expired,login')
        return AnonymousUser(), 'JWT Token has expired.'

    # print(user)
    return User.objects.get(username=payload["username"]), 'Authenticated'

# @login_required
# @csrf_exempt
def index(request):

    # payload = get_user_by_token(request.headers['Authorization'])

    # print("payload")
    # print(payload)

    # request.user, code = get_user_by_token(request)
    # print(request.user)
    # print(type(request.user))

    # if request.user.is_authenticated:
        # print("AUTENTICADOoOOOOOOOOOOOO")

    return render(request, 'home.html')

class validation():
    data = ''
    errors = ''
    def __init__(self, data, errors):
        self.data = data
        self.errors = errors

def is_questao_valid(data, questao):
    if questao is None:
        serializer = QuestaoSerializer(data=data)
    else:
        serializer = QuestaoSerializer(questao, data=data)
    
    if serializer.is_valid():
        q_created = serializer.save()
        if 'tags' not in data.keys():
            return False, validation('', {'tags':["This field is required."]})
        if type(data['tags']) is not list:
            return False, validation('', {'tags':["This field must be a list of strings."]})
        for each_field in data['tags']:
            if type(each_field) is not str:
                return False, validation('', {'tags':["This field must be a list of strings: "+str(each_field)+" is not a string."]})
        q_created.add_tags(data['tags'])
        q_created.save()
        return True, serializer
    return False, serializer

## QUESTAO VIEWS
# @csrf_exempt
@csrf_exempt
def questao_list(request):

    if request.method == 'GET':
        questoes = Questao.objects.all()
        serializer = QuestaoSerializer(questoes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request.user, code = get_user_by_token(request)
        if request.user.is_authenticated:
            data = JSONParser().parse(request)
            data['user_id'] = request.user.id
            questao_valid, serializer = is_questao_valid(data, None)           
            if questao_valid:
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({'Error':"User not logged in. " + code},status=401)

@csrf_exempt
def image_view(request, image_name):

    image = Questao.objects.get(imagem=image_name).imagem
    # resized_img = image #Handle resizing here

    return HttpResponse(image, content_type="image/png")

@csrf_exempt
def questao_send_image(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    print(request.user)

    try:
        questao = Questao.objects.get(id=pk)
    except Questao.DoesNotExist:
        return HttpResponse(status=404)

    # @login_required
    request.user, code = get_user_by_token(request)
    if request.user.is_authenticated:
        # Checking if the question belongs to the user
        if questao.user_id.id == request.user.id:
            if request.method == 'POST':

                image_file = request.FILES['imagem']
                print(request.POST.keys())
                # print(request.FILES)
                # print(request.DATA)
                # questao.imagem.save('teste.png',image_file)
                questao.imagem.save(str(request.user.username) + '_' + str(pk) +'.png',image_file)
                return JsonResponse({'message':'Image uploaded.'}, status=201)

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
        serializer = QuestaoSerializer(questao)
        return JsonResponse(serializer.data)
    
    # @login_required
    request.user, code = get_user_by_token(request)
    if request.user.is_authenticated:
        # Checking if the question belongs to the user
        if questao.user_id.id == request.user.id:
            if request.method == 'PUT':
                data = JSONParser().parse(request)
                data['user_id'] = request.user.id
                
                questao_valid, serializer = is_questao_valid(data, questao)           
                if questao_valid:
                    return JsonResponse(serializer.data, status=201)
                else:
                    return JsonResponse(serializer.errors, status=400)

            elif request.method == 'DELETE':
                questao.delete()
                return HttpResponse(status=204)
        else:
            return JsonResponse({'Error':"Questão pertence a outro usuário"},status=401)
    else:
        return JsonResponse({'Error':"User not logged in. " + code},status=401)

## TAG VIEWS
@csrf_exempt
def tag_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def tag_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        tag = Tag.objects.get(id=pk)
    except Tag.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return JsonResponse(serializer.data)

@csrf_exempt
def tag_search(request, search):
    """
    Retrieve, update or delete a code snippet.
    """
    tag_list = Tag.objects.filter(nome__contains=search)
    print(tag_list)
    if request.method == 'GET':
        serializer = TagSerializer(tag_list, many=True)
        return JsonResponse(serializer.data, safe=False)


# Caderno Views:
#----------------
# OK 1. Criar um caderno caderno/create/ -> POST
# OK 2. Editar meu caderno caderno/edit/:id -> PUT
# OK 3. Deletar meu caderno caderno/delete/:id -> DELETE
# 4. Adicionar Questões ao caderno: /caderno/:id_caderno/add/:id_questao -> POST
# 5. Remover Questões do caderno: /caderno/:id_caderno/remove/:id_questao -> POST
# OK 6. Retornar meus cadernos: caderno/:username
# Ok 7. Retorna todos os cadernos do banco: caderno/

# Retorna todos os cadernos do banco
@csrf_exempt
def caderno_get_all(request):
    if request.method == 'GET':
        cadernos = Caderno.objects.all()
        serializer = CadernoSerializer(cadernos, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retorna os cadernos de um usuario: caderno/:username
@csrf_exempt
def caderno_get_by_user(request, username):
    
    if request.method == 'GET':
        try:
            user_query = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'Error':"Username nao existe."},status=404)
        
        cadernos = Caderno.objects.filter(criador_id=user_query.id)
        serializer = CadernoSerializer(cadernos, many=True)
        return JsonResponse(serializer.data, safe=False)

# Criar um novo caderno: caderno/create
@csrf_exempt
def caderno_create(request):

    # if request.method == 'GET':
    #     return HttpResponse("Caderno Create View")
    # return render(request, 'home.html', {'user': request.user.username})

    if request.method == 'POST':
        request.user, code = get_user_by_token(request)
        print(request.user)
        if request.user.is_authenticated:
            data = JSONParser().parse(request)
            data['criador_id'] = request.user.id
            serializer = CadernoSerializer(data=data)           
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({'Error':"User not logged in. " + code},status=401)

# Editar os campos de um caderno: caderno/edit/:id
@csrf_exempt
def caderno_edit(request, pk):
    
    if request.method == 'PUT':
        request.user, code = get_user_by_token(request)
        print(request.user)
        if request.user.is_authenticated:

            try:
                caderno = Caderno.objects.get(id=pk)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao existe."},status=404)

            try:
                caderno = Caderno.objects.get(id=pk, criador_id=request.user.id)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao pertence ao usuario" + code},status=404)

            data = JSONParser().parse(request)
            # print(caderno)
            # data['criador_id'] = request.user.id
            serializer = CadernoSerializerPut(caderno, data=data)

            if serializer.is_valid():
                serializer.save()
                serializer = CadernoSerializer(caderno)
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({'Error':"User not logged in. " + code},status=401)

    if request.method == 'GET':
        try:
            caderno = Caderno.objects.get(id=pk)
        except Caderno.DoesNotExist:
            return JsonResponse({'Error':"Caderno nao existe."},status=404)

        serializer = CadernoSerializer(caderno)
        return JsonResponse(serializer.data)

    if request.method == 'DELETE':
        request.user, code = get_user_by_token(request)
        print(request.user)
        if request.user.is_authenticated:

            try:
                caderno = Caderno.objects.get(id=pk)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao existe."},status=404)

            try:
                caderno = Caderno.objects.get(id=pk, criador_id=request.user.id)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao pertence ao usuario"},status=401)

            caderno.delete()
            return HttpResponse(status=204)

        else:
            return JsonResponse({'Error':"User not logged in. " + code},status=401)

# Adicionar Questões ao caderno: /caderno/:id_caderno/add/:id_questao
@csrf_exempt
def caderno_add_questao(request, id_caderno, id_questao):
    if request.method == 'POST':
        request.user, code = get_user_by_token(request)
        print(request.user)
        if request.user.is_authenticated:
            try:
                caderno = Caderno.objects.get(id=id_caderno)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao existe."},status=404)

            try:
                caderno = Caderno.objects.get(id=id_caderno, criador_id=request.user.id)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao pertence ao usuario"},status=401)

            try:
                questao = Questao.objects.get(id=id_questao)
            except Questao.DoesNotExist:
                return JsonResponse({'Error':"Questao nao existe"},status=404)

            # Testa se a questao ja esta no caderno:
            try:
                CadQuest = RelacaoCadernoQuestao.objects.get(caderno_id=caderno, questao_id=questao)
            except RelacaoCadernoQuestao.DoesNotExist:
                #Se nao estiver, adiciona ao caderno:
                CadQuest = RelacaoCadernoQuestao(caderno_id=caderno, questao_id=questao)
                CadQuest.save()
            
            serializer = CadernoSerializer(caderno)
            return JsonResponse(serializer.data)


        else:
            return JsonResponse({'Error':"User not logged in. " + code},status=401)

@csrf_exempt
def caderno_rm_questao(request, id_caderno, id_questao):
    if request.method == 'DELETE':
        request.user, code = get_user_by_token(request)
        print(request.user)
        if request.user.is_authenticated:
            try:
                caderno = Caderno.objects.get(id=id_caderno)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao existe."},status=404)

            try:
                caderno = Caderno.objects.get(id=id_caderno, criador_id=request.user.id)
            except Caderno.DoesNotExist:
                return JsonResponse({'Error':"Caderno nao pertence ao usuario"},status=401)

            try:
                questao = Questao.objects.get(id=id_questao)
            except Questao.DoesNotExist:
                return JsonResponse({'Error':"Questao nao existe"},status=404)

            # Testa se a questao ja esta no caderno:
            try:
                CadQuest = RelacaoCadernoQuestao.objects.get(caderno_id=caderno, questao_id=questao)
            except RelacaoCadernoQuestao.DoesNotExist:
                #Se nao estiver, adiciona ao caderno:
                return JsonResponse({'Error':"Questao nao estava vinculada ao caderno."},status=404)

            
            CadQuest.delete()
            serializer = CadernoSerializer(caderno)
            return JsonResponse(serializer.data, status=200)

        else:
            return JsonResponse({'Error':"User not logged in. " + code},status=401)


@csrf_exempt
def search_view(request):
    if request.method == 'GET':
        # f_param = request.GET.get('f', '')
        # q_param = request.GET
        
        keys = request.GET.keys()

        if 'f' in keys:
            url_query = request.GET.get('f', '')
            print(url_query)
            tags_to_search = url_query.split('area~')[1:]

            print(tags_to_search)

            tag_id = int(tags_to_search[0])
            tag_obj = get_object_or_404(Tag, id=tag_id)
            query_set = QuestaoTags.objects.filter(tag_id=tag_obj)
            print(query_set)

            for tag in tags_to_search[1:]:
                tag_id = int(tag)
                tag_obj = get_object_or_404(Tag, id=tag_id)
                query_set = query_set.filter(tag_id=tag_obj)
            
            # print(query_set)
            for a in query_set:
                print(a)
                print('')

        # print(keys)
        return JsonResponse({"Message":"Bombou"}, status=200)