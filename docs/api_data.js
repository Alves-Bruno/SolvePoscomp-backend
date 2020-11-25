define({ "api": [
  {
    "type": "post",
    "url": "/auth/login/",
    "title": "Loga o usuário no sistema.",
    "name": "PostLogin",
    "group": "Auth",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "X-CSRFToken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Login do usuario.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Senha do usuario.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n\"username\": \"user\",\n\"password\": \"hardpassword\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Cookie",
            "optional": false,
            "field": "csrftoken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Success 200",
            "type": "TokenJWT",
            "optional": false,
            "field": "token",
            "description": "<p>Token JWT retornado para o login.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "user",
            "description": "<p>User fields.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "user.pk",
            "description": "<p>Id do user.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.username",
            "description": "<p>Username do user.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.email",
            "description": "<p>Email do user.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.first_name",
            "description": "<p>Not used.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.last_name",
            "description": "<p>Not used.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 204 No Content\n{\n\"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMiwidXNlcm5hbWUiOiJicnVubyIsImV4cCI6MTYwNjI1NTUyMywiZW1haWwiOiJiZGFsdmVzQGluZi51ZnNtLmJyIn0.mNiMW2PmMiRj6g9Dg1L7ULEt-yGFuhnjDR14AAvoiTo\",\n\"user\": {\n    \"pk\": 22,\n    \"username\": \"user\",\n    \"email\": \"mail@mail.com\",\n    \"first_name\": \"\",\n    \"last_name\": \"\"\n}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "    HTTP/1.1 400 Bad Request\n{\n\"non_field_errors\": [\n    \t\t\"Unable to log in with provided credentials.\"\n]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Auth"
  },
  {
    "type": "post",
    "url": "/auth/logout/",
    "title": "Desloga o usuário no sistema.",
    "name": "PostLogout",
    "group": "Auth",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "X-CSRFToken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "Cookie",
            "optional": false,
            "field": "csrftoken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "Cookie",
            "optional": false,
            "field": "sessionid",
            "description": "<p>retornada pela requisicao de login.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "detail",
            "description": "<p>Mensagem de logout.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 200 Ok\n{\n\"detail\": \"Successfully logged out.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Auth"
  },
  {
    "type": "post",
    "url": "/auth/registration/",
    "title": "Cria um novo usuario.",
    "name": "Postregistration",
    "group": "Auth",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "X-CSRFToken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Nome de usuario.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email de cadastro.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password1",
            "description": "<p>Senha do usuario.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password2",
            "description": "<p>Confirmacao de senha.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n\"username\": \"user\",\n\"email\": \"validemail@mail.com\",\n\"password1\": \"hardpassword\",\n\"password2\": \"hardpassword\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Cookie",
            "optional": false,
            "field": "csrftoken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Success 200",
            "type": "TokenJWT",
            "optional": false,
            "field": "token",
            "description": "<p>Token JWT retornado para o login.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "user",
            "description": "<p>User fields.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "user.pk",
            "description": "<p>Id do user.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.username",
            "description": "<p>Username do user.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.email",
            "description": "<p>Email do user.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.first_name",
            "description": "<p>Not used.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "user.last_name",
            "description": "<p>Not used.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 204 No Content\n{\n\"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMiwidXNlcm5hbWUiOiJicnVubyIsImV4cCI6MTYwNjI1NTUyMywiZW1haWwiOiJiZGFsdmVzQGluZi51ZnNtLmJyIn0.mNiMW2PmMiRj6g9Dg1L7ULEt-yGFuhnjDR14AAvoiTo\",\n\"user\": {\n    \"pk\": 22,\n    \"username\": \"user\",\n    \"email\": \"mail@mail.com\",\n    \"first_name\": \"\",\n    \"last_name\": \"\"\n}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Auth"
  },
  {
    "type": "post",
    "url": "/caderno/:id_caderno/add/:id_questao",
    "title": "Adiciona uma nova questao ao caderno.",
    "name": "CadernoAddQuestao",
    "group": "Caderno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "criador_id",
            "description": "<p>Id do criador(user) do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "questoes",
            "description": "<p>Lista de questoes adicionadas ao caderno.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 200 Ok\n{\n  \"id\": 5,\n  \"nome\": \"Novo Caderno\",\n  \"descricao\": \"Caderno com questoes maneiras.\",\n  \"criador_id\": 22,\n  \"questoes\": []\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"User not logged in. Authorization Header required.\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"Caderno nao pertence ao usuario\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Caderno nao existe.\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Questao nao existe.\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Questao nao estava vinculada ao caderno.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "post",
    "url": "/caderno/create",
    "title": "Cria um caderno para o user logado.",
    "name": "CadernoCreate",
    "group": "Caderno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome que o novo caderno deve receber.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "descricao",
            "description": "<p>Descricao que o novo caderno deve receber.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n\"nome\": \"Novo Caderno\",\n\"descricao\": \"Caderno com questoes maneiras.\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "criador_id",
            "description": "<p>Id do criador(user) do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "questoes",
            "description": "<p>Lista de questoes adicionadas ao caderno.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 200 Ok\n{\n  \"id\": 5,\n  \"nome\": \"Novo Caderno\",\n  \"descricao\": \"Caderno com questoes maneiras.\",\n  \"criador_id\": 22,\n  \"questoes\": []\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"User not logged in. Authorization Header required.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "delete",
    "url": "/caderno/:id_caderno",
    "title": "Deleta o caderno do usuario.",
    "name": "CadernoDelete",
    "group": "Caderno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 204 No Content\n{\n\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"User not logged in. Authorization Header required.\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"Caderno nao pertence ao usuario\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Caderno nao existe.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "post",
    "url": "/caderno/:id_caderno",
    "title": "Altera um dos campos do caderno (nome ou descricao).",
    "name": "CadernoEdit",
    "group": "Caderno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome do caderno.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "descricao",
            "description": "<p>Descricao do caderno.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n\"nome\":\"Caderno 2020\",\n    \"descricao\":\"Descricao\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "criador_id",
            "description": "<p>Id do criador(user) do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "questoes",
            "description": "<p>Lista de questoes adicionadas ao caderno.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 200 Ok\n{\n  \"id\": 5,\n  \"nome\": \"Novo Caderno\",\n  \"descricao\": \"Caderno com questoes maneiras.\",\n  \"criador_id\": 22,\n  \"questoes\": []\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"User not logged in. Authorization Header required.\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"Caderno nao pertence ao usuario\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Caderno nao existe.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "get",
    "url": "/caderno/",
    "title": "Retorna todos os cadernos do banco de dados.",
    "name": "CadernoGetAll",
    "group": "Caderno",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "criador_id",
            "description": "<p>Id do criador(user) do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "questoes",
            "description": "<p>Lista de questoes adicionadas ao caderno.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 200 Ok\n    {\n[\n  {\n    \"id\": 1,\n    \"nome\": \"Primeiro Caderno\",\n    \"descricao\": \"\",\n    \"criador_id\": 22,\n    \"questoes\": [\n      {\n        \"id\": 1,\n        \"texto\": \"Questão 31 - 2020: Bla bla\",\n        \"imagem\": null,\n        \"alternativa_correta\": \"A\",\n        \"ano\": 2002,\n        \"tags\": [\n          {\n            \"id\": 1,\n            \"nome\": \"Matemática\"\n          },\n          {\n            \"id\": 2,\n            \"nome\": \"Fundamentos da Computação\"\n          },\n          {\n            \"id\": 3,\n            \"nome\": \"Tecnologia da Computação\"\n          }\n        ],\n        \"created_at\": \"2020-11-17T20:58:00.515Z\",\n        \"updated_at\": \"2020-11-20T18:08:38.747Z\",\n        \"user_id\": 22\n      },\n    }",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "get",
    "url": "/caderno/:caderno_id",
    "title": "Retorna o caderno de acordo com o id fornecido.",
    "name": "CadernoGetById",
    "group": "Caderno",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n\n    \"id\": 2,\n    \"nome\": \"Caderno 2020\",\n    \"descricao\": \"Caderno com questoes adasdasda.\",\n    \"criador_id\": 22,\n    \"questoes\": []\n\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Caderno nao existe.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "get",
    "url": "/caderno/:username",
    "title": "Retorna todos os cadernos de um determinado user.",
    "name": "CadernoGetByUser",
    "group": "Caderno",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "criador_id",
            "description": "<p>Id do criador(user) do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "questoes",
            "description": "<p>Lista de questoes adicionadas ao caderno.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 200 Ok\n    {\n[\n  {\n    \"id\": 1,\n    \"nome\": \"Primeiro Caderno\",\n    \"descricao\": \"\",\n    \"criador_id\": 22,\n    \"questoes\": [\n      {\n        \"id\": 1,\n        \"texto\": \"Questão 31 - 2020: Bla bla\",\n        \"imagem\": null,\n        \"alternativa_correta\": \"A\",\n        \"ano\": 2002,\n        \"tags\": [\n          {\n            \"id\": 1,\n            \"nome\": \"Matemática\"\n          },\n          {\n            \"id\": 2,\n            \"nome\": \"Fundamentos da Computação\"\n          },\n          {\n            \"id\": 3,\n            \"nome\": \"Tecnologia da Computação\"\n          }\n        ],\n        \"created_at\": \"2020-11-17T20:58:00.515Z\",\n        \"updated_at\": \"2020-11-20T18:08:38.747Z\",\n        \"user_id\": 22\n      },\n    }",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Username nao existe.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "delete",
    "url": "/caderno/:id_caderno/rm/:id_questao",
    "title": "Remove uma das questaos (já cadastrada) do caderno.",
    "name": "CadernoRemoveQuestao",
    "group": "Caderno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "criador_id",
            "description": "<p>Id do criador(user) do caderno.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "questoes",
            "description": "<p>Lista de questoes adicionadas ao caderno.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 200 Ok\n{\n  \"id\": 5,\n  \"nome\": \"Novo Caderno\",\n  \"descricao\": \"Caderno com questoes maneiras.\",\n  \"criador_id\": 22,\n  \"questoes\": []\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"User not logged in. Authorization Header required.\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"Caderno nao pertence ao usuario\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Caderno nao existe.\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 404 Not Found\n{\n  \"Error\": \"Questao nao existe.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Caderno"
  },
  {
    "type": "delete",
    "url": "/questao/:questao_id/",
    "title": "Deleta os dados da questao por id.",
    "name": "DeleteQuestao_id",
    "group": "Questao",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "X-CSRFToken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          },
          {
            "group": "Parameter",
            "type": "Cookie",
            "optional": false,
            "field": "csrftoken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 204 No Content",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Questao"
  },
  {
    "type": "get",
    "url": "/questao/",
    "title": "Retorna todas as questões do banco de dados",
    "name": "GetQuestao",
    "group": "Questao",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "Questao",
            "description": "<p>Lista com todas as questoes do banco.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.id",
            "description": "<p>Id da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.texto",
            "description": "<p>Texto da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.imagem",
            "description": "<p>Nome do arquivo de imagem enviado pelo user.</p>"
          },
          {
            "group": "Success 200",
            "type": "Char",
            "optional": false,
            "field": "Questao.alternativa_correta",
            "description": "<p>Char representando a alternativa correta[&quot;A&quot;-&quot;E&quot;].</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.ano",
            "description": "<p>Ano da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "Questao.tags",
            "description": "<p>Todas as tags cadastradas para a questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.tags.id",
            "description": "<p>Id da tag.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.tags.nome",
            "description": "<p>Nome da tag.</p>"
          },
          {
            "group": "Success 200",
            "type": "DateField",
            "optional": false,
            "field": "Questao.created_at",
            "description": "<p>Data de criacao da Questao (Timezone: America/SaoPaulo).</p>"
          },
          {
            "group": "Success 200",
            "type": "DateField",
            "optional": false,
            "field": "Questao.updated_at",
            "description": "<p>Data da ultima modificação da Questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.user_id",
            "description": "<p>Id do usuario que criou a questao.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    [\n    {\n        \"id\": 1,\n        \"texto\": \"Questão 31 - 2020: Qual o nome do bla bla? a) a b) b c) c d) d e) e\",\n        \"imagem\": null,\n        \"alternativa_correta\": \"A\",\n        \"ano\": 2002,\n        \"tags\": [\n        {\n            \"id\": 1,\n            \"nome\": \"Matemática\"\n        },\n        {\n            \"id\": 2,\n            \"nome\": \"Fundamentos da Computação\"\n        },\n        {\n            \"id\": 3,\n            \"nome\": \"Tecnologia da Computação\"\n        }\n        ],\n        \"created_at\": \"2020-11-17T20:58:00.515Z\",\n        \"updated_at\": \"2020-11-20T18:08:38.747Z\",\n        \"user_id\": 22\n    },...\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Questao"
  },
  {
    "type": "get",
    "url": "/questao/:questao_id/",
    "title": "Retorna questao por id.",
    "name": "GetQuestao_id",
    "group": "Questao",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    {\n        \"id\": 1,\n        \"texto\": \"Questão 31 - 2020: Qual o nome do bla bla? a) a b) b c) c d) d e) e\",\n        \"imagem\": null,\n        \"alternativa_correta\": \"A\",\n        \"ano\": 2002,\n        \"tags\": [\n        {\n            \"id\": 1,\n            \"nome\": \"Matemática\"\n        },\n        {\n            \"id\": 2,\n            \"nome\": \"Fundamentos da Computação\"\n        },\n        {\n            \"id\": 3,\n            \"nome\": \"Tecnologia da Computação\"\n        }\n        ],\n        \"created_at\": \"2020-11-17T20:58:00.515Z\",\n        \"updated_at\": \"2020-11-20T18:08:38.747Z\",\n        \"user_id\": 22\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Questao"
  },
  {
    "type": "post",
    "url": "/questao/",
    "title": "Cadastra uma nova questao para o user logado.",
    "name": "PostQuestao",
    "group": "Questao",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "X-CSRFToken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          },
          {
            "group": "Parameter",
            "type": "Cookie",
            "optional": false,
            "field": "csrftoken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "texto",
            "description": "<p>Texto de descricao da questao.</p>"
          },
          {
            "group": "Parameter",
            "type": "ImageField",
            "optional": false,
            "field": "imagem",
            "defaultValue": "null",
            "description": "<p>Texto de descricao da questao.</p>"
          },
          {
            "group": "Parameter",
            "type": "Char",
            "optional": false,
            "field": "alternativa_correta",
            "description": "<p>Char representando a alternativa correta[&quot;A&quot;-&quot;E&quot;].</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user_id",
            "description": "<p>Id do usuario.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object[]",
            "optional": false,
            "field": "tags",
            "description": "<p>Lista de Strings que devem ser adicionadas como tags a Questao.</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "tags.string",
            "description": "<p>Caso a tag fornecida não exista, uma nova sera criada.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "    {\n\"texto\": \"Questão 31 - 2020: Questao muito importante. a) la la b) la la c) la la d) la la e) la la \",\n\"imagem\": null,\n\"alternativa_correta\": \"a\",\n\"ano\": 2002,\n\"user_id\":22,\n\"tags\": [\"Matemática\", \"Pipoca\"]\n    }",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "Questao",
            "description": "<p>Lista com todas as questoes do banco.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.id",
            "description": "<p>Id da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.texto",
            "description": "<p>Texto da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.imagem",
            "description": "<p>Nome do arquivo de imagem enviado pelo user.</p>"
          },
          {
            "group": "Success 200",
            "type": "Char",
            "optional": false,
            "field": "Questao.alternativa_correta",
            "description": "<p>Char representando a alternativa correta[&quot;A&quot;-&quot;E&quot;].</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.ano",
            "description": "<p>Ano da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "Questao.tags",
            "description": "<p>Todas as tags cadastradas para a questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.tags.id",
            "description": "<p>Id da tag.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.tags.nome",
            "description": "<p>Nome da tag.</p>"
          },
          {
            "group": "Success 200",
            "type": "DateField",
            "optional": false,
            "field": "Questao.created_at",
            "description": "<p>Data de criacao da Questao (Timezone: America/SaoPaulo).</p>"
          },
          {
            "group": "Success 200",
            "type": "DateField",
            "optional": false,
            "field": "Questao.updated_at",
            "description": "<p>Data da ultima modificação da Questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.user_id",
            "description": "<p>Id do usuario que criou a questao.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    HTTP/1.1 201 Created\n{\n\"id\": 35,\n\"texto\": \"Questão 31 - 2020: Questao muito importante. a) la la b) la la c) la la d) la la e) la la\",\n\"imagem\": null,\n\"alternativa_correta\": \"A\",\n\"ano\": 2002,\n\"tags\": [\n{\n\"id\": 1,\n\"nome\": \"Matemática\"\n},\n{\n\"id\": 33,\n\"nome\": \"Teste\"\n}\n],\n\"created_at\": \"2020-11-22T18:07:18.500Z\",\n\"updated_at\": \"2020-11-23T19:16:27.538Z\",\n\"user_id\": 22\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 401 Unauthorized\n{\n  \"Error\": \"User not logged in.\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Questao"
  },
  {
    "type": "put",
    "url": "/questao/:questao_id/",
    "title": "Altera os dados da questao por id.",
    "name": "PutQuestao_id",
    "group": "Questao",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "X-CSRFToken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          },
          {
            "group": "Parameter",
            "type": "Header",
            "optional": false,
            "field": "Authentication",
            "description": "<p>Bearer <JWT-Token recebido no login>.</p>"
          },
          {
            "group": "Parameter",
            "type": "Cookie",
            "optional": false,
            "field": "csrftoken",
            "description": "<p>csrftoken para submissao de formularios.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.id",
            "description": "<p>Id da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.texto",
            "description": "<p>Texto da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.imagem",
            "description": "<p>Nome do arquivo de imagem enviado pelo user.</p>"
          },
          {
            "group": "Success 200",
            "type": "Char",
            "optional": false,
            "field": "Questao.alternativa_correta",
            "description": "<p>Char representando a alternativa correta[&quot;A&quot;-&quot;E&quot;].</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.ano",
            "description": "<p>Ano da questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "Questao.tags",
            "description": "<p>Todas as tags cadastradas para a questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.tags.id",
            "description": "<p>Id da tag.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Questao.tags.nome",
            "description": "<p>Nome da tag.</p>"
          },
          {
            "group": "Success 200",
            "type": "DateField",
            "optional": false,
            "field": "Questao.created_at",
            "description": "<p>Data de criacao da Questao (Timezone: America/SaoPaulo).</p>"
          },
          {
            "group": "Success 200",
            "type": "DateField",
            "optional": false,
            "field": "Questao.updated_at",
            "description": "<p>Data da ultima modificação da Questao.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Questao.user_id",
            "description": "<p>Id do usuario que criou a questao.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 201 Created\n{\n    {\n        \"id\": 1,\n        \"texto\": \"Questão 31 - 2020: Qual o nome do bla bla? a) a b) b c) c d) d e) e\",\n        \"imagem\": null,\n        \"alternativa_correta\": \"A\",\n        \"ano\": 2002,\n        \"tags\": [\n        {\n            \"id\": 1,\n            \"nome\": \"Matemática\"\n        },\n        {\n            \"id\": 2,\n            \"nome\": \"Fundamentos da Computação\"\n        },\n        {\n            \"id\": 3,\n            \"nome\": \"Tecnologia da Computação\"\n        }\n        ],\n        \"created_at\": \"2020-11-17T20:58:00.515Z\",\n        \"updated_at\": \"2020-11-20T18:08:38.747Z\",\n        \"user_id\": 22\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "AppSolvePoscomp/documentation.py",
    "groupTitle": "Questao"
  }
] });
