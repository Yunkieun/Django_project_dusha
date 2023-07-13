from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'), # 질문등록
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), # 답변등록
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'), # 질문삭제
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),  # 질문수정
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),  # 답변삭제
    path('board/answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),  # 답변수정
    path('event', views.event, name='event'),  # 답변수정
    # 공지사항
    path('notice/', views.notice_list, name='notice_list'),
    path('notice/<int:notice_id>/', views.detail, name='notice_detail'),
    path('notice/create/', views.notice_create, name='notice_create'),
    path('notice/delete/<int:notice_id>/', views.notice_delete, name='notice_delete'),
    path('notice/modify/<int:notice_id>/', views.notice_modify, name='notice_modify'),

    path('service/', views.service, name='service'),

]