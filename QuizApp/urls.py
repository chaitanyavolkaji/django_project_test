from django.urls import path, re_path

from . import views

urlpatterns = [
    path("quiz", views.QuizView.as_view()),
    path("quiz/add", views.add_quiz_page),
    path("quiz/<int:id>/question/add", views.QuestionView.as_view()),

    ### Auth ###
    path("login", views.LoginView.as_view()),
]