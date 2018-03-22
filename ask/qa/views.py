from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

# Create your views here.

# def test(request, *args, **kwargs):
#     return HttpResponse('OK')
from .models import Question
from .models import Answer


@require_GET
def index(request):
	latest_question_list = Question.objects.order_by('-id')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(latest_question_list, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	context = {
		'latest_question_list': page.object_list,
		'paginator': paginator,
		'page': page,
		}
	return render(request, 'qa/index.html', context)

@require_GET
def popular(request):
	popular_question_list = Question.objects.order_by('rating')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(popular_question_list, limit)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page)
	context = {
		'popular_question_list': page.object_list,
		'paginator': paginator,
		'page': page,
		}
	return render(request, 'qa/popular.html', context)

@require_GET
def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	answers = Answer.objects.filter(question=question.id)
	context = {
	'question':	question,
	'answers':	answers,
	}
	return render(request, 'qa/question.html', context)