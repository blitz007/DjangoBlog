from django.forms import ModelForm
from .models import Post,Comment

class PostForm(ModelForm):

	class Meta:
		model=Post
		fields = ('topic','content',)

class CommentForm(ModelForm):

	class Meta:
		model=Comment
		fields=('text',)

'''class LikePostForm(ModelForm):

	class Meta:
		model=Post
		fields=('votes',)
		exclude=('topic','content','pub_date')'''