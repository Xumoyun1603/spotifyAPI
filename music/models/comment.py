from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()


class Comment(models.Model):
    song_id = models.ForeignKey(
        'music.Song', on_delete=models.CASCADE, related_name='comments'
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)

