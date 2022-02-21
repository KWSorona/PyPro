from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import Photo
from django.core.paginator import Paginator


def index(request):
    photos_all = Photo.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(photos_all, '9')
    photos = paginator.page(page)
    return render(request, 'polls/index.html', {"photos": photos})


def generic(request):
    return render(request, 'polls/generic.html')


def wc(request):
    return render(request, 'polls/wellcome.html')

# loader 사용 시
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# 404 error 넣은 예제
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
