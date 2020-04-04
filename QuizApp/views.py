from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views import View
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse

from QuizApp.models import Quiz, Question, Answer

from  .serializers import QuizSerializer, QuestionSerializer

class LoginView(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/quizapp/quiz")
        return render(request, "login.html")

    def post(self, request):
        user = authenticate(request, username=request.data["username"], password=request.data["password"])
        if user is not None:
            login(request, user)
            return redirect("/quizapp/quiz")
        return render(request, "login.html")

class QuizView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        context = {'quizzes': serializer.data}
        return render(request, "quizzes.html", context)

    def post(self, request, *args, **kwargs):

        quiz = Quiz(name=request.data["name"])
        quiz.save()
        context = {"name" : quiz.name, "id" : quiz.id}
        return render(request, "question_add.html", context)

class QuestionView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        quiz = Quiz.objects.get(pk=id)

        questions = Question.objects.filter(quiz=quiz)

        serializer = QuestionSerializer(questions, many=True)
        context = {"name" : quiz.name, "id" : quiz.id, 'questions': serializer.data}
        return render(request, "question_add.html", context)

    def post(self, request, id):

        quiz = Quiz.objects.get(pk=id)
        question = Question(description=request.data["description"],
                            quiz=quiz, correct_option=request.data["correct_option"])
        question.save()

        option_a = Answer(description=request.data["option_a"], option="A")
        option_a.question = question
        option_a.save()

        option_b = Answer(description=request.data["option_b"], option="B")
        option_b.question = question
        option_b.save()

        option_c = Answer(description=request.data["option_c"], option="C")
        option_c.question = question
        option_c.save()

        option_d = Answer(description=request.data["option_d"], option="D")
        option_d.question = question
        option_d.save()

        questions = Question.objects.filter(quiz=quiz)

        serializer = QuestionSerializer(questions, many=True)
        context = {"name" : quiz.name, "id" : quiz.id, 'questions': serializer.data}
        return render(request, "question_add.html", context)


def add_quiz_page(request):
    return render(request, "quiz_add.html")

def add_question_page(request):
    return render(request, "question_add.html")