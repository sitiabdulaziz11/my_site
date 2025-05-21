from django.db import models

from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    """Author model
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    

    def __str__(self):
        """display format for Author.
        """
        return f"{self.first_name} {self.last_name}, {self.email}"

class Tag(models.Model):
    """Tag model
    """
    caption = models.CharField(max_length=30)
    
    def __str__(self):
        """display format for Author.
        """
        return f"{self.caption}"

class Post(models.Model):
    """Post models
    """
    title = models.CharField(max_length=250)
    excerpt = models.CharField(max_length=300)
    # image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post", null=True)
    # date = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        """To display posts in a correct format.
        """
        return self.title
    
    # def post_display(self):
    #     """Post contentes.
    #     """
    #     return f"{self.title} {self.excerpt} {self.date} {self.slug} {self.content} {self.author}" # {self.tag}"
    
    # def __str__(self):
    #     """ Display format for post.
    #     """
    #     return self.post_display()

class Comment(models.Model):
    """Comment model
    """
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField(max_length=254)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateField(auto_now=True)

