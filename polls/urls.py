from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import QuestionViewSet, ChoiceViewSet


router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('api/', include(router.urls)),  # API path
    path('api1/', views.question_list)  # Raw API path
]