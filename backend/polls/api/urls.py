from django.urls import path
from .views import PollViewSet, QuestionViewSet, ChoiceViewSet, UsersTestViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet)
router.register('questions', QuestionViewSet)
router.register('choices', ChoiceViewSet)
router.register('users_answer', UsersTestViewSet)

urlpatterns = router.urls
