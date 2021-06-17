from django.urls import path
from .views import HomePageView, NewsMainView, NewsArticleView, CreateNewsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("news/", NewsMainView.as_view(), name="news-main"),
    path("news/create/", CreateNewsView.as_view(), name="create"),
    path("news/<int:article_id>/", NewsArticleView.as_view(), name="news-article"),
]
