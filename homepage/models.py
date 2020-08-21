from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=280)
    boast_roast = models.BooleanField()
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']

    def counter_of_votes(self):
        return self.upvote - self.downvote
