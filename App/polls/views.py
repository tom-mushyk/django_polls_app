from django.shortcuts import render, redirect
from .models import Question, Choice

def index(request):
    questions = Question.objects.order_by('-pub_date')
    context = { 
        'questions': questions 
        }
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = { 
        'question': question,
        }
    return render(request, 'polls/results.html', context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    choices = question.choice_set.all()
    if request.method == 'POST':
        _choice = request.POST.get('choice_radio')
        choice = Choice.objects.get(choice_text = _choice) 
        choice.votes += 1
        choice.save()
        return redirect('results', question_id=question_id)
            
    context = { 
        'question': question,
        'choices': choices,
        }
    return render(request, 'polls/detail.html', context)

