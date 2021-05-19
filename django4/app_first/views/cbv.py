from django.shortcuts import render
from django.http import HttpResponse
from app_first.models import Post
from app_first.forms import PostForm
from django.views import View


class PostLISTAPI(View):

    def get(self, request):
        data = Post.objects.all().values()

        return render(request, 'posts.html', {"data": data})

class PostCreateAPI(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form)
            form.save()
        return render(request, 'create_post.html', {'form': form})

class PostDeleteUpdateAPI(View):

    def delete(self, request, id):
        data = Post.objects.get(id=id)
        data.delete()
        return HttpResponse("<p>deleted<p>")

    def get(self, request, id):
        data = Post.objects.get(id=id)
        form = PostForm(instance=data)
        return render(request, "create_post.html", {'form': form})

    def post(self, request, id):
        data = Post.objects.get(id=id)
        form = PostForm(instance=data, data=request.POST)
        if form.is_valid():
            form.save()
