from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_id = models.CharField(max_length=50, unique=True)
    channel_id = models.CharField(max_length=50)
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()
    channel_title = models.CharField(max_length=255)

    class Meta:
        ordering = ["-published_at"]
        indexes = [
            models.Index(fields=["video_id", "-published_at"]),
            models.Index(fields=["channel_id", "-published_at"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["video_id", "channel_id"], name="unique_video"
            )
        ]
        db_table = "video"

    def __str__(self):
        return self.title
