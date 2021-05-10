from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from polls.models import Question, Choice


def home(request):
    return HttpResponse("<h1> home page </h1>")

def question(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, "polls/question.html", {'latest_question_list': latest_question_list})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question_id=question_id)
    return render(request, "polls/index.html", {'question': question, 'choices': choices})

def votes(request,question_id):
    print(request.POST)
    question = Question.objects.get(id=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(f"/polls/{question_id}/results/")

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, "polls/results.html", {"question": question})