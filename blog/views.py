from django.shortcuts import get_object_or_404,render
from .models import Post,Comment
from .forms import CommentForm

def index(request):
	latest_list=Post.objects.order_by('-pub_date')
	return render(request,'blog/index.html', {'latest_list':latest_list})


def detail(request, post_id):
		post=get_object_or_404(Post, pk=post_id)
		return render(request, 'blog/detail.html',{'post':post})

def add_comment_to_post(request,post_id):
	post=get_object_or_404(Post,pk=post_id)
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment = form.save()
			comment.save()
			return redirect('blog/detail.html',pk=post_id)
		else:
			form = CommentForm()
		return render(request, 'blog/add_comment_to_post.html',{'form':form})


# Create your views here.
