from .models import Subject,Chapters,Topics,Content
from django import forms

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class ChaptersForm(forms.ModelForm):
    class Meta:
        model = Chapters
        fields = ['chapter_name','subject']
        widgets = {
            'subject': forms.CheckboxSelectMultiple(),
        }

class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['topic_name','subject','chapter']
        widgets = {
            'subject': forms.CheckboxSelectMultiple(),
            'chapter': forms.CheckboxSelectMultiple(),
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['notes','document','subject','chapter','topics']
        widgets = {
            'subject':forms.CheckboxSelectMultiple(),
            'chapter':forms.CheckboxSelectMultiple(),
            'topics':forms.CheckboxSelectMultiple(),
        }