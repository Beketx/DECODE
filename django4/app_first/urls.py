from django.urls import path
from app_first.views import main_page, cv, post_detailed, post_list, \
                            create_post, update_post,delete_post,\
                            PostLISTAPI, PostCreateAPI, PostDeleteUpdateAPI,\
                            LoginView, LogoutViewCustom, RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', main_page, name='main_url'),
    path('my_cv', cv),
    path('posts', post_list, name='posts_list_url'),
    path('create_post', create_post),
    path('posts/<int:id>', post_detailed, name='post_detail_url'),
    path('update_post/<int:id>', update_post),
    path('delete_post/<int:id>', delete_post),
    path('class_posts/', PostLISTAPI.as_view()),
    path('create_class_post/', PostCreateAPI.as_view()),
    path('update_delete/<int:id>', PostDeleteUpdateAPI.as_view()),

    path('login/', LoginView.as_view(), name='login_url'),
    # path('logout/', LogoutView.as_view(), name='logout_url'),
    path('logout/', LogoutViewCustom.as_view(), name='logout_url'),
    path('register', RegisterView.as_view(), name='register_url')
]