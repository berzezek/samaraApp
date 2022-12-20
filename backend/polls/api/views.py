from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Poll, Question, Choice, UsersTest
from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, ChoiceGetSerializer, UsersTestSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        questions = Question.objects.filter(poll=instance)
        questions_serializer = QuestionSerializer(questions, many=True)
        return Response({'poll': serializer.data, 'questions': questions_serializer.data})


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        choices = Choice.objects.filter(question=instance)
        choices_serializer = ChoiceGetSerializer(choices, many=True)
        return Response({'question': serializer.data, 'choices': choices_serializer.data})


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersTestViewSet(viewsets.ModelViewSet):
    queryset = UsersTest.objects.all()
    serializer_class = UsersTestSerializer
    permission_classes = [permissions.IsAuthenticated]
