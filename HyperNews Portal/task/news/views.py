import json
import random
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View


def get_news_data():
    """Return data from news.json as a JSON object."""
    with open("hypernews/news.json", "r") as json_data:
        return json.load(json_data)


# Create a view for the home page.
class HomePageView(View):
    def get(self, request):
        return HttpResponse("<h1>Coming soon</h1>")


# Create a view for the news main page.
class NewsMainView(View):
    def get(self, request):
        news = get_news_data()
        # Sort the news articles by date, newest first.
        sorted_news = sorted(news, key=lambda x: x["created"], reverse=True)
        return render(request, "news/index.html", context={"sorted_news": sorted_news})


# Create a view for the news articles.
class NewsArticleView(View):
    def get(self, request, article_id):
        news = get_news_data()
        # Assign the first news article to the variable 'article'.
        article = news[0]
        # Iterate through each news article and update 'article' if the article_id matches the link to the news article.
        for news_article in news:
            if news_article["link"] == article_id:
                article = news_article
                break
        return render(request, "news/article.html", context=article)


# Create a view to add news articles.
class CreateNewsView(View):
    def get(self, request):
        return render(request, "news/create.html")

    def post(self, request, *args, **kwargs):
        news = get_news_data()
        title = request.POST.get("title")
        text = request.POST.get("text")
        # Generate a unique link.
        link = random.randint(1, 9999999)
        while link in [news_article["link"] for news_article in news]:
            link = random.randint(1, 9999999)
        # Update JSON file.
        created_article = [
            {
                "created": str(datetime.now())[:19],
                "text": text,
                "title": title,
                "link": link,
            },
        ]
        data = news + created_article
        with open("hypernews/news.json", "w") as news_data:
            json.dump(data, news_data)
        # Redirect to news home page.
        return redirect("/news/")
