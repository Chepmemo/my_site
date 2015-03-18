from .models import Question, Choice
from .serializer import ChoiceSerializer, QuestionSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class QuestionList(APIView):
    def get(self, request, format=None):
        question = Question.objects.all()
        serialized_question = QuestionSerializer(question, many=True)
        return Response(serialized_question.data)


class ChoiceList(APIView):
    def get(self, request, format=None):
        choice = Choice.objects.all()
        serialized_choice = ChoiceSerializer(choice, many=True)
        return Response(serialized_choice.data)


class QuestionDetail(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = Question.objects.filter(pk=pk)
        serialized_question = QuestionSerializer(question, many=True)
        return Response(serialized_question.data)


class ChoiceDetail(APIView):
    def get_object(self, pk):
        try:
            return Choice.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        choice = Choice.objects.filter(pk=pk)
        serialized_choice = ChoiceSerializer(choice, many=True)
        return Response(serialized_choice.data)
