from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views
from .views import QuestionViewSet, ChoiceViewSet


router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
app_name = "polls"
urlpatterns = [
    # Auth URLs
    path('register/', views.register, name='register'),  # Register
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(next_page='/polls/'), name='logout'),  # Logout

    # Polls App URLs
    path('', views.index, name='index'), # main URL
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),

    # API URLs
    path('api/', include(router.urls)),  # API path
    path('api1/', views.question_list)  # Raw API path
]