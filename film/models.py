from django.db import models
from django.contrib.auth.models import User


class ActorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.name + " " + self.surname
   
class FilmModel(models.Model):
    name = models.CharField(max_length=256)
    rating = models.FloatField(default=0)
    pub_date = models.DateField(blank=True, null=True)
    views_count = models.IntegerField(default=0)
    country = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="posters/")
    video = models.FileField(upload_to="videos/")
    fragman = models.FileField(upload_to="fragmans/")
    about = models.TextField(blank=True, null=True)

    actors = models.ManyToManyField(ActorModel, related_name="films", blank=True, null=True)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"
    
    def __str__(self):
        return self.name
    
class CommentModel(models.Model):
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="used_comments")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_comments")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.user.username + " | " + self.film.name
    

class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_like")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return self.user.username + " | " + self.film.name
        
    

class ViewsCountModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_viewscount")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_viewscount")

    class Meta:
        verbose_name = "Views Count"
        verbose_name_plural = "Views Counts"
    
    def __str__(self):
        return self.user.username + " " + self.film.name