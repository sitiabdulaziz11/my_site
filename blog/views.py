from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

all_posts = [
    # {
    #     "slug": "hike-in-the-mountain",
    #     "image": "Terra db sketch.PNG",
    #     "author": "Siti",
    #     "date": date(2025, 2, 26),
    #     "title": "Mountain Hiking",
    #     "excerpt": "There's nothing Like the views you get when hiking in the Mountain! And I wasn't even prepared for what happend whilst I was enjoying the view!",
    #     "content": """
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
    #                 """
    # },
    #   {
    #     "slug": "the-mountain",
    #     "image": "budge.jpg",
    #     "author": "Siti",
    #     "date": date(2025, 4, 26),
    #     "title": "Mountain Visiting",
    #     "excerpt": "There's nothing Like the views you get when hiking in the Mountain! And I wasn't even prepared for what happend whilst I was enjoying the view!",
    #     "content": """
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
    #                 """
    # },
    # {
    #     "slug": "hike-in-mountain",
    #     "image": "sms2.PNG",
    #     "author": "Siti",
    #     "date": date(2025, 3, 26),
    #     "title": "Mountain seeing",
    #     "excerpt": "There's nothing Like the views you get when hiking in the Mountain! And I wasn't even prepared for what happend whilst I was enjoying the view!",
    #     "content": """
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
                    
    #                 At the bottom right of VS Code, ensure that the language mode is HTML or another supported language. If it shows something else like Plain Text, click on it and change it to HTML
    #                 """
    # }
]

def get_date(post):
    """
    helper function for getting the sorted date.
    """
    # return post.get('date') or
    return post['date']
    # return post['all_post']  wrrong
    # return post["date"] if post["date"] is not None else datetime.min  # ✅ Default date to handle None date value case
    
# Create your views here.

def starting_page(request):
    """Renders the home page of the blog.
    """
    # sorted_posts = posts.sort(key=get_date)
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})  # blog/index.html is b/c template part is looked by django by default. so we don't say templates/blog/index.html

    # or like below
    # posts = BlogPost.objects.all().order_by("-date")[:3]  # Get latest 3 posts
    #     return render(request, "blog/index.html", {"posts": posts})

def posts(request):
    """For one post
    """
    # return render(request, "blog/all_posts.html")
    return render(request, "blog/all_posts.html", {"whole_posts": all_posts })

def posts_detail(request, slug):
    """For one post detail.
    """ 
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    # print( f"post {identified_post}")
    return render(request, "blog/post-detail.html", {"post": identified_post })
