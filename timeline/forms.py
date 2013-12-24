#-*-coding:utf-8-*-
from django import forms
from timeline.models import TimeLine

class TimeLineForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text=u"标题:")
    summary = forms.CharField(max_length=4096, help_text=u"介绍:")
    ctime = forms.DateField(widget=forms.HiddenInput(), required=False)
    ptime = forms.DateField(widget=forms.HiddenInput(), required=False)
    privacy = forms.IntegerField(initial=1)

    class Meta:
        model = TimeLine
