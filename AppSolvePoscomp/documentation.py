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
@apiParam {Cookie} csrftoken csrftoken para submissao de formularios.
@apiParam {Cookie} sessionid retornada pela requisicao de login.
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
@apiParam {Cookie} csrftoken csrftoken para submissao de formularios.
@apiParam {Cookie} sessionid retornada pela requisicao de login.
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
@apiParam {Cookie} csrftoken csrftoken para submissao de formularios.
@apiParam {Cookie} sessionid retornada pela requisicao de login.

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
@apiSuccess {Cookie} sessionid retornada pela requisicao de login.
@apiSuccess {JWT-token} key Token JWT retornado para o login.


@apiSuccessExample {json} Success-Response:
    HTTP/1.1 204 No Content
	{
		"key": "50e041f9514d7febac14b2d71e8a9767fbf8d6ce"
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

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 Created
	{
		"key": "65dded0d703e1d77ec8c3b25f723fa11ef2aa78d"
	}
"""
