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

    return User.objects.get(username=payload["username"]), 'Authenticated'

# @login_required
def index(request):

    # payload = get_user_by_token(request.headers['Authorization'])

    # print("payload")
    # print(payload)

    request.user, code = get_user_by_token(request)
    print(request.user)
    print(type(request.user))

    if request.user.is_authenticated:
        print("AUTENTICADOoOOOOOOOOOOOO")

    return render(request, 'home.html', {'user': request.user.username})

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
            questao_valid, serializer = is_questao_valid(data, None)           
            if questao_valid:
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({'Error':"User not logged in. " + code},status=401)


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
