from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Subject,Chapters,Topics,Content
from .forms import SubjectForm,ChaptersForm,TopicsForm,ContentForm

# Create your views here.
#@login_required(login_url='/accounts/login/')
def index(request):
    #subject form
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            subject = subject_form.save(commit=False)
            subject.save
    else:
        subject_form = SubjectForm()
    #chapters form
    if request.method == 'POST':
        chapter_form = ChaptersForm(request.POST)
        if chapter_form.is_valid():
            chapter = chapter_form.save(commit=False)
            chapter.save
    else:
        chapter_form = ChaptersForm()
    #content form
    if request.method == 'POST':
        content_form = ContentForm(request.POST)
        if form.is_valid():
            content = content_form.save(commit=False)
            content.save
    else:
        content_form = ContentForm()
    #topic form
    if request.method == 'POST':
        topic_form = TopicsForm(request.POST)
        if topic_form.is_valid():
            topic = topic_form.save(commit=False)
            topic.save
    else:
        topic_form = TopicsForm()
    args = {
        "chapter_form":chapter_form,
        "subject_form":subject_form,
        "content_form":content_form,
        "topic_form":topic_form,
    }
    return render (request,'index.html',args)