from django.shortcuts import render
from main.models import Post
from main.forms import PostForm
# Create your views here.
def list_posts(request):
    context = {'posts':Post.objects.all()[:10]}
    return render(request, 'main_page.html', context)

def new_post(request):
    if request.method == 'GET':
        context = {"form": PostForm}
        return render(request, 'new.html', context)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            Post.objects.create(title=title, content=content, image=image)
            return list_posts(request)
        return render(request, 'new.html', {"form": form})