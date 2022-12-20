from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, ChoiceGetSerializer, UsersTestSerializer
from ..models import Poll, Question, Choice, UsersTest


# paginator


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        questions = Question.objects.filter(poll=instance)
        questions_serializer = QuestionSerializer(questions, many=True)
        return Response({'poll': serializer.data, 'questions': questions_serializer.data})


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        poll_id = request.query_params.get('poll')
        try:
            poll = Poll.objects.get(id=poll_id)
            queryset = Question.objects.filter(poll=poll)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Poll.DoesNotExist:
            return Response({'error': 'Poll does not exist'})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        choices = Choice.objects.filter(question=instance)
        choices_serializer = ChoiceGetSerializer(choices, many=True)
        return Response({'question': serializer.data, 'choices': choices_serializer.data})


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceGetSerializer
    pagination_class = None
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        question_id = request.query_params.get('question')
        try:
            question = Question.objects.get(id=question_id)
            queryset = Choice.objects.filter(question=question)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response({'error': 'Question does not exist'})


class UsersTestViewSet(viewsets.ModelViewSet):
    queryset = UsersTest.objects.all()
    serializer_class = UsersTestSerializer
    permission_classes = [permissions.IsAuthenticated]
