from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "slug": "hike-in-the-mountain",
        "title": "sms2.PNG",
        "author": "Siti",
        "date": date(2025, 2, 26),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing Like the views you get when hiking in the Mountain! And I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
                    At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    """
    },
    {
        "slug": "hike-in-the-mountain",
        "title": "sms2.PNG",
        "author": "Siti",
        "date": date(2025, 2, 26),
        "title": "Mountain Visiting",
        "excerpt": "There's nothing Like the views you get when hiking in the Mountain! And I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
                    At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    """
    },
    {
        "slug": "hike-in-the-mountain",
        "title": "sms2.PNG",
        "author": "Siti",
        "date": date(2025, 2, 26),
        "title": "Mountain seeing",
        "excerpt": "There's nothing Like the views you get when hiking in the Mountain! And I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
                    At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    """
    }
]

def get_date(post):
    """
    helper function for getting the sorted date.
    """
    # return post.get('date') or
    return post['post']

# Create your views here.

def starting_page(request):
    """Renders the home page of the blog.
    """
    sorted_posts = posts.sort(key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"recent_posts": latest_posts})  # blog/index.html is b/c template part is looked by django by default. so we don't say templates/blog/index.html

def posts(request):
    """For one post
    """
    return render(request, "blog/all_posts.html")

def posts_detail(request, slug):
    """For one post detail.
    """
    return render(request, "blog/post-detail.html")
 