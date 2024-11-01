from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Board,Topic,Post,User
from .forms import NewTopicForm,PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    boards=Board.objects.all()
    
    return render(request,'home.html',{'boards':boards})


def boards_topics(request,boards_name):
    board=get_object_or_404(Board,name=boards_name)
    return render(request,'topics.html',{'board_name':board})

@login_required
def new_topic(request,boards_name):
    board=get_object_or_404(Board,name=boards_name)
    form=NewTopicForm()
    if request.method == "POST":
        user=request.user
        form=NewTopicForm(request.POST)
        if form.is_valid():
            topic=form.save(commit=False)
            topic.board=board
            topic.created_by=user
            topic.save()
            post=Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=user, 
                topic=topic
            )
            return redirect('boards_topics',boards_name)
    
    return render(request,'new_topic.html',{'board_name':board,'form':form})

def topic_posts(request, boards_name, topic_id):
    topic = get_object_or_404(Topic, board__name=boards_name, pk=topic_id)
    return render(request, 'topic_posts.html', {"topic": topic})

@login_required
def reply_topic(request, boards_name, topic_id):
    topic = get_object_or_404(Topic, board__name=boards_name, pk=topic_id)
    if request.method == "POST":
        user = request.user
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = user
            post.save()
            
            return redirect('topic_posts', boards_name, topic.id)
    else:
        form = PostForm()

    return render(request, "reply_topic.html", {'topic': topic, 'form': form})