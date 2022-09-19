from django.db import models

# Create your models here.
class WatchlistItem(models.Model):
    item_watched = models.TextField()
    item_title = models.TextField()
    item_rating = models.IntegerField()
    item_release_date = models.CharField(max_length=255)
    item_review = models.TextField()