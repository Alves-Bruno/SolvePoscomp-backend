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

	url(r'^auth/', include('rest_auth.urls')),
	url(r'^auth/registration/', include('rest_auth.registration.urls')),
	url(r'^account/', include('allauth.urls')),

	#QUESTAO URLS
	path('questao/', views.questao_list),
	path('questao/<int:pk>/', views.questao_detail),

	# TAG URLS
	path('tag/', views.tag_list),
	path('tag/<int:pk>/', views.tag_detail),
	path('tag/<search>/', views.tag_search),

]