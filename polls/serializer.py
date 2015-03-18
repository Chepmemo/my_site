from .models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    """docstring for QuestionSerializer"""
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'pub_date'
            )


class ChoiceSerializer(serializers.ModelSerializer):
    """docstring for QuestionSerializer"""
    class Meta:
        model = Choice
        fields = (
            'id',
            'question',
            'choice_text',
            'votes'
            )
