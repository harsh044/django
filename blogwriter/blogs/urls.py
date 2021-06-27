
from django.urls import path
from .views import PostView,PostDetail,AddPostview,UpdatePost,DeletePost,SearchResultsView
from . import views


urlpatterns = [
    #path('', views.Post, name="Post"),
    path('/', PostView.as_view(), name="Post"),
    path('/add_post',AddPostview.as_view(),name='add_post'),
    path('/Post/<int:pk>', PostDetail.as_view(), name='PostDetail'),
    path('/Post/edit/<int:pk>',UpdatePost.as_view(),name='update_post'),
    path('/Post/<int:pk>/Delete',DeletePost.as_view(),name='delete_post'),
    path('/search', SearchResultsView.as_view(), name='search_results'),
]