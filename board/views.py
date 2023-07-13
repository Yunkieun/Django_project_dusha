from allauth.account.views import  PasswordChangeView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from board.models import Question, Answer, Notice
from board.forms import QuestionForm, AnswerForm, NoticeForm
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q


def index(request):
    print(request.user)
    return render(request, "board/index.html")

def event(request):

        return render(request, "board/event.html")

#비밀번호 변경시 인덱스 페이지로 리버스
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')

#질문 목록
def question_list(request):
    #question_list = Question.objects.all()
    page =request.GET.get('page', 1)
    kw = request.GET.get('kw', '')

    question_list = Question.objects.order_by('-create_date')
    if  kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains =kw)|
            Q(answer__content__icontains=kw)).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 설정
    page_obj = paginator.get_page(page)  # 페이지 가져오기
    context = {'question_list': page_obj, 'page': page, 'kw': kw}

    return render(request, 'board/question_list.html', context)


def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) # 데이터가 없으면 404 처리
    context = {'question' : question}
    return render(request, 'board/detail.html', context)

# 질문 등록
@login_required(login_url='/login/') # 로그인 페이지로 이동
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST) # 입력된 데이터가 있는 폼
        if form.is_valid(): # 폼이 유효성 검사를 통과했다면
            question = form.save(commit=False) #가저장
            question.author = request.user # 세션 권한(로그인한) 있는 글쓴이
            question.create_date = timezone.now()  #등록일 생성
            form.save() #진짜로 저장
            return redirect('board:question_list') # 질문 목록 페이지 이동

    else:  #get 방식
        form = QuestionForm()  #폼 객체 생성(빈 폼 생성)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)  # get 방식

# 답변 등록
@login_required(login_url='/login/')
def answer_create(request, question_id):

    # question = Question.objects.get(id=question_id) #해당 id의 질문 객체 생성
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)  # 입력값 전달받음
        if form.is_valid():
            answer = form.save(commit=False)  # 내용만 저장됨
            answer.create_date = timezone.now()  # 작성일
            answer.author = request.user  # 세션 발급
            answer.question = question  # 외래키 질문 저장
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board/detail.html', context)


# 질문수정
@login_required(login_url='/login/')
def question_modify(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)


# 질문 삭제
@login_required(login_url='/login/')
def question_delete(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:question_list')


# 답변 삭제
@login_required(login_url='/login/')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()

# 답변 수정
@login_required(login_url='/login/')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('board:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'board/answer_form.html', context)

#공지사항

def notice_list(request):
    #question_list = Question.objects.all()
    page =request.GET.get('page', 1)
    kw = request.GET.get('kw', '')

    notice_list = Notice.objects.order_by('-create_date')
    if  kw:
        notice_list = notice_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw)).distinct()

    paginator = Paginator(notice_list, 10)  # 페이지당 10개씩 설정
    page_obj = paginator.get_page(page)  # 페이지 가져오기
    context = {'notice_list': page_obj, 'page': page, 'kw': kw}

    return render(request, 'board/notice_list.html', context)


def notice_detail(request, notice_id):
    #question = Question.objects.get(id=question_id)
    notice = get_object_or_404(Notice, id=notice_id) # 데이터가 없으면 404 처리
    context = {'notice' : notice}
    return render(request, 'board/notice_detail.html', context)


# 질문 등록
def is_admin(user):
    return user.is_superuser or user.username == '123'

@user_passes_test(is_admin)
def notice_create(request):
    if request.method == "POST":
        form = NoticeForm(request.POST) # 입력된 데이터가 있는 폼
        if form.is_valid(): # 폼이 유효성 검사를 통과했다면
            notice = form.save(commit=False) #가저장
            notice.author = request.user # 세션 권한(로그인한) 있는 글쓴이
            notice.create_date = timezone.now()  #등록일 생성
            form.save() #진짜로 저장
            return redirect('board:notice_list') # 질문 목록 페이지 이동

    else:  #get 방식
        form = NoticeForm()  #폼 객체 생성(빈 폼 생성)
    context = {'form': form}
    return render(request, 'board/notice_form.html', context)  # get 방식

# 공지사항수정
@login_required(login_url='/login/')
def notice_modify(request, notice_id):

    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.modify_date = timezone.now()
            notice.save()
            return redirect('board:detail', notice_id=notice.id)
    else:
        form = NoticeForm(instance=notice)
    context = {'form': form}
    return render(request, 'board/notice_form.html', context)


# 질문 삭제
@login_required(login_url='/login/')
def notice_delete(request, notice_id):

    notice = get_object_or_404(Notice, pk=notice_id)
    notice.delete()
    return redirect('board:notice_list')




def service(request):
    return render(request, "board/service.html")

