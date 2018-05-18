from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Subject,Chapters,Topics,Content
from .forms import SubjectForm,ChaptersForm,TopicsForm,ContentForm

# Create your views here.
#@login_required(login_url='/accounts/login/')
def index(request):
    test = "Working!!"
    return render (request,'index.html',{"test":test})

def new_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save
        else:
            form = SubjectForm()
    return render(request,'subject.html',{"form":form})

def new_chapter(request):
    if request.method == 'POST':
        form = ChaptersForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.save
    else:
        form = ChaptersForm()
    return render(request,'chapter.html',{"form":form})

def new_topic(request):
    if request.method == 'POST':
        form = TopicsForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.save
        else:
            form = TopicsForm()
    return render(request,'topic.html',{"form":form})

def new_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.save
        else:
            form = ContentForm()
    return render(request,'content.html',{"form":form})