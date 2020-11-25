"""
--> QUESTAO GET ALL <--
@api {get} /questao/ Retorna todas as questões do banco de dados
@apiName GetQuestao
@apiGroup Questao

@apiSuccess {Object[]} Questao  Lista com todas as questoes do banco.
@apiSuccess {Number} Questao.id  Id da questao.
@apiSuccess {String} Questao.texto  Texto da questao.
@apiSuccess {String} Questao.imagem  Nome do arquivo de imagem enviado pelo user.
@apiSuccess {Char} Questao.alternativa_correta  Char representando a alternativa correta["A"-"E"].
@apiSuccess {Number} Questao.ano  Ano da questao.
@apiSuccess {Object[]} Questao.tags  Todas as tags cadastradas para a questao.
@apiSuccess {Number} Questao.tags.id  Id da tag.
@apiSuccess {String} Questao.tags.nome  Nome da tag.
@apiSuccess {DateField} Questao.created_at  Data de criacao da Questao (Timezone: America/SaoPaulo).
@apiSuccess {DateField} Questao.updated_at  Data da ultima modificação da Questao.
@apiSuccess {Number} Questao.user_id  Id do usuario que criou a questao.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
        {
            "id": 1,
            "texto": "Questão 31 - 2020: Qual o nome do bla bla? a) a b) b c) c d) d e) e",
            "imagem": null,
            "alternativa_correta": "A",
            "ano": 2002,
            "tags": [
            {
                "id": 1,
                "nome": "Matemática"
            },
            {
                "id": 2,
                "nome": "Fundamentos da Computação"
            },
            {
                "id": 3,
                "nome": "Tecnologia da Computação"
            }
            ],
            "created_at": "2020-11-17T20:58:00.515Z",
            "updated_at": "2020-11-20T18:08:38.747Z",
            "user_id": 22
        },...
    }
 
"""
"""
--> QUESTAO POST <--
@api {post} /questao/ Cadastra uma nova questao para o user logado.
@apiName PostQuestao
@apiGroup Questao
@apiParam {Header} X-CSRFToken csrftoken para submissao de formularios.
@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.
@apiParam {Cookie} csrftoken csrftoken para submissao de formularios.
@apiParam {String} texto  Texto de descricao da questao.
@apiParam {ImageField} imagem=null  Texto de descricao da questao.
@apiParam {Char} alternativa_correta  Char representando a alternativa correta["A"-"E"].
@apiParam {Number} user_id  Id do usuario.
@apiParam {Object[]} tags  Lista de Strings que devem ser adicionadas como tags a Questao. 
@apiParam {string} tags.string Caso a tag fornecida não exista, uma nova sera criada.

@apiParamExample {json} Request-Example:
    {
	"texto": "Questão 31 - 2020: Questao muito importante. a) la la b) la la c) la la d) la la e) la la ",
	"imagem": null,
	"alternativa_correta": "a",
	"ano": 2002,
	"user_id":22,
	"tags": ["Matemática", "Pipoca"]
    }

@apiSuccess {Object[]} Questao  Lista com todas as questoes do banco.
@apiSuccess {Number} Questao.id  Id da questao.
@apiSuccess {String} Questao.texto  Texto da questao.
@apiSuccess {String} Questao.imagem  Nome do arquivo de imagem enviado pelo user.
@apiSuccess {Char} Questao.alternativa_correta  Char representando a alternativa correta["A"-"E"].
@apiSuccess {Number} Questao.ano  Ano da questao.
@apiSuccess {Object[]} Questao.tags  Todas as tags cadastradas para a questao.
@apiSuccess {Number} Questao.tags.id  Id da tag.
@apiSuccess {String} Questao.tags.nome  Nome da tag.
@apiSuccess {DateField} Questao.created_at  Data de criacao da Questao (Timezone: America/SaoPaulo).
@apiSuccess {DateField} Questao.updated_at  Data da ultima modificação da Questao.
@apiSuccess {Number} Questao.user_id  Id do usuario que criou a questao.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 Created
	{
	"id": 35,
	"texto": "Questão 31 - 2020: Questao muito importante. a) la la b) la la c) la la d) la la e) la la",
	"imagem": null,
	"alternativa_correta": "A",
	"ano": 2002,
	"tags": [
		{
		"id": 1,
		"nome": "Matemática"
		},
		{
		"id": 33,
		"nome": "Teste"
		}
	],
	"created_at": "2020-11-22T18:07:18.500Z",
	"updated_at": "2020-11-23T19:16:27.538Z",
	"user_id": 22
	}

@apiErrorExample {json} Error-Response:
    HTTP/1.1 401 Unauthorized
    {
      "Error": "User not logged in."
    }

"""

"""
--> QUESTAO GET BY_ID <--
@api {get} /questao/:questao_id/ Retorna questao por id.
@apiName GetQuestao_id
@apiGroup Questao

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        {
            "id": 1,
            "texto": "Questão 31 - 2020: Qual o nome do bla bla? a) a b) b c) c d) d e) e",
            "imagem": null,
            "alternativa_correta": "A",
            "ano": 2002,
            "tags": [
            {
                "id": 1,
                "nome": "Matemática"
            },
            {
                "id": 2,
                "nome": "Fundamentos da Computação"
            },
            {
                "id": 3,
                "nome": "Tecnologia da Computação"
            }
            ],
            "created_at": "2020-11-17T20:58:00.515Z",
            "updated_at": "2020-11-20T18:08:38.747Z",
            "user_id": 22
        }
    }

@apiErrorExample {json} Error-Response:
    HTTP/1.1 404 Not Found
 
"""

"""
--> QUESTAO PUT BY_ID <--
@api {put} /questao/:questao_id/ Altera os dados da questao por id.
@apiName PutQuestao_id
@apiGroup Questao

@apiParam {Header} X-CSRFToken csrftoken para submissao de formularios.
@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.
@apiParam {Cookie} csrftoken csrftoken para submissao de formularios.
@apiSuccess {Number} Questao.id  Id da questao.
@apiSuccess {String} Questao.texto  Texto da questao.
@apiSuccess {String} Questao.imagem  Nome do arquivo de imagem enviado pelo user.
@apiSuccess {Char} Questao.alternativa_correta  Char representando a alternativa correta["A"-"E"].
@apiSuccess {Number} Questao.ano  Ano da questao.
@apiSuccess {Object[]} Questao.tags  Todas as tags cadastradas para a questao.
@apiSuccess {Number} Questao.tags.id  Id da tag.
@apiSuccess {String} Questao.tags.nome  Nome da tag.
@apiSuccess {DateField} Questao.created_at  Data de criacao da Questao (Timezone: America/SaoPaulo).
@apiSuccess {DateField} Questao.updated_at  Data da ultima modificação da Questao.
@apiSuccess {Number} Questao.user_id  Id do usuario que criou a questao.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 Created
    {
        {
            "id": 1,
            "texto": "Questão 31 - 2020: Qual o nome do bla bla? a) a b) b c) c d) d e) e",
            "imagem": null,
            "alternativa_correta": "A",
            "ano": 2002,
            "tags": [
            {
                "id": 1,
                "nome": "Matemática"
            },
            {
                "id": 2,
                "nome": "Fundamentos da Computação"
            },
            {
                "id": 3,
                "nome": "Tecnologia da Computação"
            }
            ],
            "created_at": "2020-11-17T20:58:00.515Z",
            "updated_at": "2020-11-20T18:08:38.747Z",
            "user_id": 22
        }
    }

@apiErrorExample {json} Error-Response:
    HTTP/1.1 404 Not Found
 
"""


"""
--> QUESTAO DELETE BY_ID <--
@api {delete} /questao/:questao_id/ Deleta os dados da questao por id.
@apiName DeleteQuestao_id
@apiGroup Questao

@apiParam {Header} X-CSRFToken csrftoken para submissao de formularios.
@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.
@apiParam {Cookie} csrftoken csrftoken para submissao de formularios.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 204 No Content


@apiErrorExample {json} Error-Response:
    HTTP/1.1 404 Not Found
 
"""

"""
--> LOGIN <--
@api {post} /auth/login/ Loga o usuário no sistema.
@apiName PostLogin
@apiGroup Auth

@apiParam {Header} X-CSRFToken csrftoken para submissao de formularios.
@apiParam {String} username Login do usuario.
@apiParam {String} password Senha do usuario.

@apiParamExample {json} Request-Example:
	{
		"username": "user",
		"password": "hardpassword"
	}

@apiSuccess {Cookie} csrftoken csrftoken para submissao de formularios.
@apiSuccess {TokenJWT} token Token JWT retornado para o login.
@apiSuccess {Object[]} user User fields.
@apiSuccess {Number} user.pk Id do user.
@apiSuccess {String} user.username Username do user.
@apiSuccess {String} user.email Email do user.
@apiSuccess {String} user.first_name Not used.
@apiSuccess {String} user.last_name Not used.


@apiSuccessExample {json} Success-Response:
    HTTP/1.1 204 No Content
    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMiwidXNlcm5hbWUiOiJicnVubyIsImV4cCI6MTYwNjI1NTUyMywiZW1haWwiOiJiZGFsdmVzQGluZi51ZnNtLmJyIn0.mNiMW2PmMiRj6g9Dg1L7ULEt-yGFuhnjDR14AAvoiTo",
    "user": {
        "pk": 22,
        "username": "user",
        "email": "mail@mail.com",
        "first_name": "",
        "last_name": ""
    }
    }

@apiErrorExample {json} Error-Response:
    HTTP/1.1 400 Bad Request
	{
		"non_field_errors": [
    		"Unable to log in with provided credentials."
		]
	}
"""

"""
--> LOGOUT <--
@api {post} /auth/logout/ Desloga o usuário no sistema.
@apiName PostLogout
@apiGroup Auth

@apiParam {Header} X-CSRFToken csrftoken para submissao de formularios.
@apiParam {Cookie} csrftoken csrftoken para submissao de formularios.
@apiParam {Cookie} sessionid retornada pela requisicao de login.

@apiSuccess {String} detail Mensagem de logout.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
	{
		"detail": "Successfully logged out."
	}
"""

"""
--> REGISTRATION <--
@api {post} /auth/registration/ Cria um novo usuario.
@apiName Postregistration
@apiGroup Auth

@apiParam {Header} X-CSRFToken csrftoken para submissao de formularios.
@apiParam {String} username Nome de usuario.
@apiParam {String} email Email de cadastro.
@apiParam {String} password1 Senha do usuario.
@apiParam {String} password2 Confirmacao de senha.

@apiParamExample {json} Request-Example:
	{
		"username": "user",
		"email": "validemail@mail.com",
		"password1": "hardpassword",
		"password2": "hardpassword"
	}

@apiSuccess {Cookie} csrftoken csrftoken para submissao de formularios.
@apiSuccess {TokenJWT} token Token JWT retornado para o login.
@apiSuccess {Object[]} user User fields.
@apiSuccess {Number} user.pk Id do user.
@apiSuccess {String} user.username Username do user.
@apiSuccess {String} user.email Email do user.
@apiSuccess {String} user.first_name Not used.
@apiSuccess {String} user.last_name Not used.


@apiSuccessExample {json} Success-Response:
    HTTP/1.1 204 No Content
    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMiwidXNlcm5hbWUiOiJicnVubyIsImV4cCI6MTYwNjI1NTUyMywiZW1haWwiOiJiZGFsdmVzQGluZi51ZnNtLmJyIn0.mNiMW2PmMiRj6g9Dg1L7ULEt-yGFuhnjDR14AAvoiTo",
    "user": {
        "pk": 22,
        "username": "user",
        "email": "mail@mail.com",
        "first_name": "",
        "last_name": ""
    }
    }
"""



"""
--> CADERNO GET ALL <--
@api {get} /caderno/ Retorna todos os cadernos do banco de dados.
@apiName CadernoGetAll
@apiGroup Caderno

@apiSuccess {Number} id Id do caderno.
@apiSuccess {String} nome Nome do caderno.
@apiSuccess {Number} criador_id Id do criador(user) do caderno.
@apiSuccess {Object[]} questoes Lista de questoes adicionadas ao caderno.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
    {
[
  {
    "id": 1,
    "nome": "Primeiro Caderno",
    "descricao": "",
    "criador_id": 22,
    "questoes": [
      {
        "id": 1,
        "texto": "Questão 31 - 2020: Bla bla",
        "imagem": null,
        "alternativa_correta": "A",
        "ano": 2002,
        "tags": [
          {
            "id": 1,
            "nome": "Matemática"
          },
          {
            "id": 2,
            "nome": "Fundamentos da Computação"
          },
          {
            "id": 3,
            "nome": "Tecnologia da Computação"
          }
        ],
        "created_at": "2020-11-17T20:58:00.515Z",
        "updated_at": "2020-11-20T18:08:38.747Z",
        "user_id": 22
      },
    }
"""

"""
--> CADERNO GET BY USER <--
@api {get} /caderno/:username Retorna todos os cadernos de um determinado user.
@apiName CadernoGetByUser
@apiGroup Caderno

@apiSuccess {Number} id Id do caderno.
@apiSuccess {String} nome Nome do caderno.
@apiSuccess {Number} criador_id Id do criador(user) do caderno.
@apiSuccess {Object[]} questoes Lista de questoes adicionadas ao caderno.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
    {
[
  {
    "id": 1,
    "nome": "Primeiro Caderno",
    "descricao": "",
    "criador_id": 22,
    "questoes": [
      {
        "id": 1,
        "texto": "Questão 31 - 2020: Bla bla",
        "imagem": null,
        "alternativa_correta": "A",
        "ano": 2002,
        "tags": [
          {
            "id": 1,
            "nome": "Matemática"
          },
          {
            "id": 2,
            "nome": "Fundamentos da Computação"
          },
          {
            "id": 3,
            "nome": "Tecnologia da Computação"
          }
        ],
        "created_at": "2020-11-17T20:58:00.515Z",
        "updated_at": "2020-11-20T18:08:38.747Z",
        "user_id": 22
      },
    }

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Username nao existe."
}
"""

"""
--> Caderno by id <--
@api {get} /caderno/:caderno_id Retorna o caderno de acordo com o id fornecido.
@apiName CadernoGetById
@apiGroup Caderno

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
    {

        "id": 2,
        "nome": "Caderno 2020",
        "descricao": "Caderno com questoes adasdasda.",
        "criador_id": 22,
        "questoes": []

    }

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Caderno nao existe."
}
"""

"""
--> CREATE CADERNO <--
@api {post} /caderno/create Cria um caderno para o user logado.
@apiName CadernoCreate
@apiGroup Caderno

@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.
@apiParam {String} nome Nome que o novo caderno deve receber.
@apiParam {String} descricao Descricao que o novo caderno deve receber.

@apiParamExample {json} Request-Example:
{
	"nome": "Novo Caderno",
	"descricao": "Caderno com questoes maneiras."
}

@apiSuccess {Number} id Id do caderno.
@apiSuccess {String} nome Nome do caderno.
@apiSuccess {Number} criador_id Id do criador(user) do caderno.
@apiSuccess {Object[]} questoes Lista de questoes adicionadas ao caderno.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
{
  "id": 5,
  "nome": "Novo Caderno",
  "descricao": "Caderno com questoes maneiras.",
  "criador_id": 22,
  "questoes": []
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "User not logged in. Authorization Header required."
}
"""

"""
--> CADERNO ADD QUESTAO <--
@api {post} /caderno/:id_caderno/add/:id_questao Adiciona uma nova questao ao caderno.
@apiName CadernoAddQuestao
@apiGroup Caderno

@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.

@apiSuccess {Number} id Id do caderno.
@apiSuccess {String} nome Nome do caderno.
@apiSuccess {Number} criador_id Id do criador(user) do caderno.
@apiSuccess {Object[]} questoes Lista de questoes adicionadas ao caderno.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
{
  "id": 5,
  "nome": "Novo Caderno",
  "descricao": "Caderno com questoes maneiras.",
  "criador_id": 22,
  "questoes": []
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "User not logged in. Authorization Header required."
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "Caderno nao pertence ao usuario"
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Caderno nao existe."
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Questao nao existe."
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Questao nao estava vinculada ao caderno."
}
"""

"""
--> CADERNO REMOVE QUESTAO <--
@api {delete} /caderno/:id_caderno/rm/:id_questao Remove uma das questaos (já cadastrada) do caderno.
@apiName CadernoRemoveQuestao
@apiGroup Caderno

@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.

@apiSuccess {Number} id Id do caderno.
@apiSuccess {String} nome Nome do caderno.
@apiSuccess {Number} criador_id Id do criador(user) do caderno.
@apiSuccess {Object[]} questoes Lista de questoes adicionadas ao caderno.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
{
  "id": 5,
  "nome": "Novo Caderno",
  "descricao": "Caderno com questoes maneiras.",
  "criador_id": 22,
  "questoes": []
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "User not logged in. Authorization Header required."
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "Caderno nao pertence ao usuario"
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Caderno nao existe."
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Questao nao existe."
}
"""

"""
--> CADERNO EDICAO <--
@api {post} /caderno/:id_caderno Altera um dos campos do caderno (nome ou descricao).
@apiName CadernoEdit
@apiGroup Caderno

@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.
@apiParam {String} nome Nome do caderno.
@apiParam {String} descricao Descricao do caderno.

@apiParamExample {json} Request-Example:
{
	"nome":"Caderno 2020",
    "descricao":"Descricao"
}

@apiSuccess {Number} id Id do caderno.
@apiSuccess {String} nome Nome do caderno.
@apiSuccess {Number} criador_id Id do criador(user) do caderno.
@apiSuccess {Object[]} questoes Lista de questoes adicionadas ao caderno.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 Ok
{
  "id": 5,
  "nome": "Novo Caderno",
  "descricao": "Caderno com questoes maneiras.",
  "criador_id": 22,
  "questoes": []
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "User not logged in. Authorization Header required."
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "Caderno nao pertence ao usuario"
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Caderno nao existe."
}
"""

"""
--> CADERNO DELETE <--
@api {delete} /caderno/:id_caderno Deleta o caderno do usuario.
@apiName CadernoDelete
@apiGroup Caderno

@apiParam {Header} Authentication Bearer <JWT-Token recebido no login>.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 204 No Content
    {

    }

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "User not logged in. Authorization Header required."
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 401 Unauthorized
{
  "Error": "Caderno nao pertence ao usuario"
}

@apiErrorExample {json} Success-Response:
    HTTP/1.1 404 Not Found
{
  "Error": "Caderno nao existe."
}
"""
