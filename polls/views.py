from django.shortcuts import render, redirect, HttpResponse
from .models import Poll, Uservoted
from django.contrib.auth.models import User
import json
from django.contrib.auth.decorators import login_required


@login_required(login_url='register')
def create_poll(request):
    if request.method == 'POST':
        options = request.POST.getlist('poll_options')
        votes = request.POST.getlist('votes')
        description = request.POST['poll-description']
        new_poll = Poll(poll_title=description,
                        user=request.user, options=options, votes=votes)
        new_poll.save()
        return redirect('/')
    else:
        return render(request, 'create-poll.html')


@login_required(login_url='register')
def display_polls(request):
    all_polls=Poll.objects.order_by(('time_created'))
    voted = Uservoted.objects.filter(user=request.user).values('poll')
    return render(request, 'display-polls.html', {'all_polls': all_polls,'voted':voted})


@login_required(login_url='register')
def display_single_poll(request):
    poll_id = request.GET['id']
    poll = Poll.objects.get(id=poll_id)
    if Uservoted.objects.filter(user=request.user, poll=poll).exists():
        already_voted = True
    else:
        already_voted = False
    return render(request, 'single-poll.html', {'poll': poll, 'already_voted': already_voted})


@login_required(login_url='register')
def vote_up(request):
    if request.method == 'POST':

        votes = json.loads(request.POST['votes'])
        poll_id = request.POST['poll_id']
        option_chosen = request.POST['option_chosen']

        poll = Poll.objects.get(id=poll_id)
        poll.votes = votes
        poll.save()

        user_vote = Uservoted(user=request.user, poll=poll,option_chosen=option_chosen)
        user_vote.save()

        votes = json.dumps(poll.votes)
        return HttpResponse(votes)


@login_required(login_url='register')
def user_polls(request):
    user_polls = Poll.objects.filter(user=request.user).order_by('time_created')
    return render(request, 'user_polls.html', {'user_polls': user_polls})


@login_required(login_url='register')
def poll_results(request):
    poll_id = request.GET['id']
    poll = Poll.objects.get(id=poll_id)
    return render(request, 'poll_results.html', {'poll': poll})


@login_required(login_url='register')
def username_validate(request):
    username=request.POST['username']
    if User.objects.filter(username=username).exists():
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def delete_poll(request):
    poll=Poll.objects.get(id=request.POST['id'])
    poll.delete()
    return redirect('user_polls')
