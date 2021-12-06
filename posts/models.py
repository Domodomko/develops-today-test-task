from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    link = models.URLField(max_length=100, verbose_name="Link")
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation Date"
    )
    upvotes_ammount = models.PositiveIntegerField(
        default=0, verbose_name="Upvotes Ammount"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")

    def __str__(self):
        return self.title

    def author_name(self):
        return f"{self.author.first_name} {self.author.last_name}"


class Comment(models.Model):
    content = models.TextField(max_length=1000, verbose_name="Content")
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation Date"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments", verbose_name="Author"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Post"
    )

    def __str__(self):
        return f"Comment by {self.author} for {self.post}"

    def author_name(self):
        return f"{self.author.first_name} {self.author.last_name}"
