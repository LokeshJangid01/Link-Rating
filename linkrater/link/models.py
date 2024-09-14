from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length = 255)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name
    
    def get_rating(self):
        if self.reviews.count():
            total_score = 0

            for review in self.reviews.all():
                total_score += review.rating

            return total_score / self.reviews.count()
        
        return 'No reviews'
    

class Review(models.Model):
    link = models.ForeignKey(Link,related_name = 'reviews',on_delete = models.CASCADE)
    link = models.ForeignKey(Link,related_name = 'reviews',on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name='reviews',on_delete = models.CASCADE)
    rating = models.IntegerField(
        validators = [MinValueValidator(1),MaxValueValidator(5)]
    )
    content = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.link.name} -{self.rating} star by {self.user.username}'
    

    

