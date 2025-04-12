from django.db import models

# Create your models here.


class Author(models.Model):
    """Author model
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    

    def __str__(self):
        """display format for Author.
        """
        return f"{self.first_name} {self.last_name}, {self.email}"

class Tag(models.Model):
    """Tag model
    """
    caption = models.CharField(max_length=300)
    
    def __str__(self):
        """display format for Author.
        """
        return f"{self.caption}"


class Post(models.Model):
    """Post models
    """
    title = models.CharField(max_length=250)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    
    
    def post_display(self):
        """Post contentes.
        """
        return f"{self.title} {self.excerpt} {self.date} {self.slug} {self.content} {self.author}" # {self.tag}"
    
    def __str__(self):
        """ Display format for post.
        """
        return self.post_display()
