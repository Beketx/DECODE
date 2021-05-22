from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app_first.models import Post, Blogger
from app_first.forms import PostForm, LoginForm, RegistrationForm
from django.views import View

from django.contrib.auth import authenticate, login, logout

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

    return render(request, 'blog/main.html', data)


def cv(request):
    return render(request, 'cv.html')


def post_list(request):
    if request.method == "GET":
        data = Post.objects.all().values()
        print(data)

    return render(request, 'blog/posts.html', {"data": data})

def post_detailed(requset, id):
    if requset.method == "GET":
        data = Post.objects.get(id=id)
        print(data.cover)
    return render(requset, 'blog/post_detailed.html', {"data": data})


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

class LoginView(View):

    def get(self, request):
        form = LoginForm(request.POST or None)
        return render(request, 'blog/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/app_first/posts')
        return render(request, 'blog/login.html',
                      context={'form': form})

class LogoutViewCustom(View):

    def get(self, request):
        form = LoginForm(request.POST or None)
        request.session.flush()
        if hasattr(request, 'user'):
            from django.contrib.auth.models import AnonymousUser
            request.user = AnonymousUser()
        return render(request, 'blog/login.html', context={'form': form})


class RegisterView(View):

    def get(self, request):
        form = RegistrationForm(request.POST)
        return render(request, 'blog/registration.html',
                      context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Blogger.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/app_first/posts')
        return render(request, 'blog/registration.html',
                      context={'form': form})


    #123123