from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Image
from .forms import PostForm
# Create your views here.

# @require_POST
# @login_required

def list(request):
    # post = get_object_or_404(Post, pk=pk)
    # if request.user == post.user:
    posts = Post.objects.all()
    return render(request,'main.html', {'posts':posts})

def write(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for img in request.FILES.getlist('image', None):
                Image.objects.create(post=post, image=img)
            return redirect('post:list')
    else:
        form=PostForm()
        return render(request,'write.html', {'form':form})
    
def show(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    # post = Post.objects.filter(Post, pk =post_id)
    images = Image.objects.filter(post=post)
    # post = Post.objects.prefetch_related('image_set').get(pk=post_id)
    return render(request, 'detail.html',{'post':post, 'images':images})