from django.db import models

class CarReview(models.Model):
    country = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    reviewer_name = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    segment = models.CharField(max_length=100)
    rating = models.FloatField()
    review_description = models.TextField()

    class Meta:
        app_label = 'carreviews'

    def __str__(self):
        return f"{self.model_name} review by {self.reviewer_name}"
