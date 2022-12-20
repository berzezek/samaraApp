from rest_framework import serializers

from polls.models import Poll, Question, Choice, UsersTest


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = 'id', 'choice_text'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class UsersTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersTest
        fields = '__all__'
