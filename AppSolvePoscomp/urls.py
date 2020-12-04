from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views
# from rest_auth.registration.views import VerifyEmailView, RegisterView
from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView
from dj_rest_auth.registration.views import VerifyEmailView
# from rest_auth.registration.views import VerifyEmailView


app_name = 'AppSolvePoscomp'
urlpatterns = [
    path('', views.index, name='index'),
	# path("questao/<int:questao_id>", views.questao_by_id, name="questao_by_id"),
	# path('questao/create', views.questao_create, name='questao_create'),

	# path('auth/', include('rest_auth.urls')),
	# path('auth/registration/', include('rest_auth.registration.urls')),

    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

	# AUTH URLS
	url(r'^auth/', include('rest_auth.urls')),
	url(r'^auth/registration/', include('rest_auth.registration.urls')),
	url(r'^account/', include('allauth.urls')),

	# url(r'^auth/token/', obtain_jwt_token),
	# url(r'^auth/token/refresh/', refresh_jwt_token),
	# url(r'^auth/token/verify/', verify_jwt_token),

	#QUESTAO URLS
	path('questao/', views.questao_list),
	path('questao/multipart/', views.questao_multipart),
	path('questao/<int:pk>/', views.questao_detail),

	path('questao/<int:pk>/imagem/', views.questao_send_image),
	path('questao/imagem/<image_name>', views.image_view),

	# TAG URLS
	path('tag/', views.tag_list),
	path('subtags/', views.tag_list_by_set),
	path('tag/<int:pk>/', views.tag_detail),
	path('tag/<search>/', views.tag_search),

	# CADERNO URLS
	path('caderno/', views.caderno_get_all),
	path('caderno/<username>', views.caderno_get_by_user),
	path('caderno/create/', views.caderno_create),
	path('caderno/<int:pk>/', views.caderno_edit),
	#/caderno/:id_caderno/add/:id_questao
	path('caderno/<int:id_caderno>/add/<int:id_questao>/', views.caderno_add_questao),
	path('caderno/<int:id_caderno>/rm/<int:id_questao>/', views.caderno_rm_questao),

	# SEARCH VIEW
	path('search/', views.search_view),
]