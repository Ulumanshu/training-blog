from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Post
        fields = ('public', 'chart_type', 'date_from', 'title', 'text')
        exclude = ('user',)

    def clean_text(self):
        text  = self.cleaned_data.get('text')
        badwords = ['fuck', 'kaka', 'audi']
        check_list = [True if w in text else False for w in badwords]
        # if title exists create slug from title
        if True in check_list:
            for word in badwords:
                text = text.replace(word, '*' * len(word))

        return text

    def save(self):
        obj = super(PostForm, self).save(commit=False)
        obj.author = self.user
        obj.save()
        return obj


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "Type Comment"
        }
