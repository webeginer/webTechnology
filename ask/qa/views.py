from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.

# def test(request, *args, **kwargs):
#     return HttpResponse('OK')
from .models import Question
#from .models import Answer
from django import forms
from .forms import AskForm
from .forms import AnswerForm


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

def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			# return HttpResponseRedirect(reverse('qa:question', args=[question_id]))
	else:
		form = AnswerForm()
		form.fields['question'] = forms.ModelChoiceField(Question.objects.filter(pk=question_id).values_list('id', flat=True), label='на вопрос №', empty_label=None)
	context = {
		'question':	question,
		'form':		form,
		}
	return render(request, 'qa/question.html', context)

def ask_add(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			return HttpResponseRedirect(reverse('qa:question', args=[question.id]))
	else:
		form = AskForm()
		context = {
		'form': form
		}
	return render(request, 'qa/ask_add.html', context)