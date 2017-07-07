from django.shortcuts import get_object_or_404,render
from .models import Post,Comment
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm


def index(request):
	latest_list=Post.objects.order_by('-pub_date')
	return render(request,'blog/index.html', {'latest_list':latest_list})


def detail(request, post_id):
		post=get_object_or_404(Post, pk=post_id)
		return render(request, 'blog/detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.pub_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
# Create your views here.
