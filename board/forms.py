from django import forms
from board.models import Question, Answer, Notice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject' : '제목',
            'content' : '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변 내용'
        }
class NoticeForm(forms.ModelForm):
    class Meta:
        model =Notice
        fields = ['subject', 'content', 'file','photo']
        labels = {
            'subject' : '제목',
            'content' : '내용',
            'file' : '파일',
            'photo' : '포토'
        }