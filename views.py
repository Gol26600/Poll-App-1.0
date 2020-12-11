from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def home_view(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, "home.html", context)


def create_view(request):
    form = PollForm()
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, "create.html", context)


def poll_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == "POST":
        print(request.POST['poll'])
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option1_count += 1
        elif selected_option == 'option2':
            poll.option2_count += 1
        elif selected_option == 'option3':
            poll.option3_count += 1
        elif selected_option == 'option4':
            poll.option4_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')
        poll.save()
        return redirect('results', poll_id)

    context = {
        'poll': poll
    }
    return render(request, "poll.html", context)


def results_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    context = {
        'poll': poll
    }
    return render(request, "results.html", context)


def stats_view(request):
    polls = Poll.objects.all()
    total_polls = polls.count()
    context = {
        'polls': polls,
        'total_polls': total_polls,
    }
    return render(request, "stats.html", context)

