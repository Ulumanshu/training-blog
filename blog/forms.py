from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('public', 'title', 'text')

    def clean_text(self):
        text  = self.cleaned_data.get('text')
        badwords = ['fuck', 'kaka', 'adsvgergewrg']
        check_list = [True if w in text else False for w in badwords]
        # if title exists create slug from title
        if True in check_list:
            for word in badwords:
                text = text.replace(word, '*' * len(word))

        return text


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "Type Comment"
        }
