from django.contrib import admin

from board.models import Question, Answer, Notice

# 관리자 페이지에 등록
admin.site.register(Question) # 질문 모델 등록
admin.site.register(Answer) # 질문 모델 등록
admin.site.register(Notice)

