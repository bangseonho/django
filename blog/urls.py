from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('post_list/new', views.post_new, name='post_new'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:pk>',views.post_detail, name='post_detail'),
    path('post_detail/<int:pk>/comment_create/',views.comment_create, name='comment_create')
]