from django.shortcuts import get_object_or_404,render
from .models import Post,Comment
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm,CommentForm,LikePostForm


def index(request):
	latest_list=Post.objects.order_by('-pub_date')
	return render(request,'blog/index.html', {'latest_list':latest_list})


def detail(request, post_id):
	post=get_object_or_404(Post,pk=post_id)
	if request.method=='POST':
		form1=CommentForm(request.POST)
		'''form=LikePostForm(request.POST)'''
		if form1.is_valid():
			comment=form1.save(commit=False)
			comment.post=post
			comment.pub_date=timezone.now()
			comment.save()
			return redirect('detail',post_id=post.id)

		'''elif form.is_valid() and not form1.is_valid():
			post=form.save(commit=False)
			post.votes+=1
			post.save()
			return redirect('detail',post_id=post.id)'''

	else:
		form1 = CommentForm()
		'''form=LikePostForm()'''
	return render(request,'blog/detail.html',{'form1':form1,'post':post,})
		
'''post=get_object_or_404(Post, pk=post_id)
return render(request, 'blog/detail.html',{'post':post})'''

def post_new(request):
    if request.method=="POST":
    	form = PostForm(request.POST)
    	if form.is_valid():
	    	post=form.save(commit=False)
	    	post.pub_date=timezone.now()
	    	post.save()
	    	return redirect('index')
    else:
    	form = PostForm()
    return render(request,'blog/post_edit.html',{'form':form,})


	


# Create your views here.
