from django import forms
from .models import Topic,Post
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