from django.db import models
from apps.login_app_the_wall.models import User
# Create your models here.
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages")
    mess_likes = models.ManyToManyField(User, related_name="mess_likes", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Message object: {self.message} ({self.id}) {self.user} {self.created_at} {self.updated_at}>"
    def total_likes(self):
        return self.mess_likes.count()

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="comments")
    message = models.ForeignKey(Message, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Comment object: {self.comment} ({self.id}) {self.user} {self.message} {self.created_at} {self.updated_at}>"

