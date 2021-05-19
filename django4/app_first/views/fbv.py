from django.shortcuts import render
from django.http import HttpResponse
from app_first.models import Post
from app_first.forms import PostForm
from django.views import View

def main_page(request): # FBV - Functional Based View
    data = {
        'desc': 'Описание из Django Views',
        'cars': ['Toyota', 'BMW', 'Mercedes', 'Honda', 'KIA', 'Chevrolet', 'Lada'],
        'phone': {
            'name': 'Iphone 12 Pro',
            'memory': '512GB',
            'brand': 'Apple'
        },
        'cars_with_img': [{
                'img': 'image/cars/car1.jpeg',
                'name': 'Toyota'
            },
            {
                'img': 'image/cars/car2.jpeg',
                'name': 'Kia'
            },
            {
                'img': 'image/cars/car3.jpeg',
                'name': 'Honda'
            }
            ]
    }

    return render(request, 'main.html', data)


def cv(request):
    return render(request, 'cv.html')


def post_list(request):
    if request.method == "GET":
        data = Post.objects.all().values()
        print(data)

    return render(request, 'posts.html', {"data": data})

def post_detailed(requset, id):
    if requset.method == "GET":
        data = Post.objects.get(id=id)
        print(data.cover)
    return render(requset, 'post_detailed.html', {"data": data})


def create_post(request):
    form = PostForm()

    if request.method == "POST":
        # print(request.POST)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form)
            form.save()

    return render(request, 'create_post.html', {'form': form})

def update_post(request, id):
    data = Post.objects.get(id=id)
    form = PostForm(instance=data)

    if request.method == "POST":
        # form = PostForm(instance={"Name": data.name, "Content": data.content, "Views": data.views}, data=request.POST)
        form = PostForm(instance=data, data=request.POST)

        if form.is_valid():
            form.save()

    return render(request, "create_post.html", {'form': form})

def delete_post(request, id):
    data = Post.objects.get(id=id)
    data.delete()
    return HttpResponse("<p>deleted<p>")