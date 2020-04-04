from rest_framework import serializers
from .models import Quiz, Question, Answer

class QuizSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['option', 'description']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [ 'description', 'answers', 'correct_option']
