from django import forms
from .models import Topic,Post,Board
class NewTopicForm(forms.ModelForm):
    message=forms.CharField(
        widget=
        forms.Textarea(
            attrs={
                'placeholder':'The Max Length Of Text Is 500',
                'class':'form-control',
                'id':"id_message",
                
                },
            ),

        max_length=500,
        help_text='The Max Length Of Text Is 500',
        )
    subject=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'',#من الضروري وضع place holder والا لن يكون هناك انميشن لليبل
                'class':'form-control',
                'id':"id_subject",
                },
            ),
        max_length=255,
        help_text="The Max Length Of Text Is 255"
    )
    class Meta:
        model=Topic
        fields=['subject','message']
        
class PostForm(forms.ModelForm):
    message=forms.CharField(
        widget=
        forms.Textarea(
            attrs={
                'placeholder':'The Max Length Of Text Is 500',
                'class':'form-control',
                'id':"id_message",
                
                },
            ),

        max_length=500,
        help_text='The Max Length Of Text Is 500',
        )
    
    class Meta():
        
        model=Post
        fields=['message']


class NewBoardForm(forms.ModelForm):
    class Meta:
        model=Board
        fields="__all__"
    
    name=forms.CharField(
        widget=
        forms.TextInput(
            attrs={
                'placeholder':'The Max Length Of Text Is 50',
                'class':'form-control',
                'id':"name",
                
                },
            ),

        max_length=50,
        help_text='The Max Length Of Text Is 50',
        )
    description=forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'',#من الضروري وضع place holder والا لن يكون هناك انميشن لليبل
                'class':'form-control',
                'id':"description",
                },
            ),
        max_length=150,
        help_text="The Max Length Of Text Is 150"
    )