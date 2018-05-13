from django.http import HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Category,Question,Choice
from django.http import HttpResponse

score = [0]
class IndexView(generic.ListView):
	template_name = 'quizzer/index.html'
	context_object_name = 'category_list'
	def get_queryset(self):
		return Category.objects.order_by('category_text')

class QuestionView(generic.DetailView):
	model = Question
	template_name = 'quizzer/detail.html'

def startquiz(request,category_id):
	question_list = Question.objects.filter(category_id=category_id)
	score = [0]
	for query in question_list:
		return render(request,'quizzer/detail.html',{'question':query,'score':0})
def quiz(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	score [0] = score [0] + 1
	print(score)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except :
		return render(request,'quizzer/detail.html',{'question':question,'error_message':"You didn't select a choice."})
	else:
		if selected_choice.iscorrect == True:
			categ = question.category.id
			question_list = Question.objects.filter(category_id=categ)
			for query in question_list:
				if query.id > question.id:
					return render(request,'quizzer/detail.html',{'question':query,'score':score[0]})
			temporary = score [0] 
			score [0] = 0
			return render(request,'quizzer/win.html',{'score':temporary})
		else:
			temporary = score [0] - 1
			score [0] = 0
			return render(request,'quizzer/gameover.html',{'score':temporary})
