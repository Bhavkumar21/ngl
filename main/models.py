from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    identifier = models.CharField(max_length=100)

    def downvote(self):
        return int(Post.objects.filter(user=self).count())

    def __str__(self):
        return self.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.content
