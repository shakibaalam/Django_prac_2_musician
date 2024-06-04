# from django.db import models

# class AlbumModel(models.Model):
#     name=models.CharField(max_length=100)
#     release_date=models.DateField()
#     rating=models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

# album/models.py
from django.db import models
from musician.models import MusicianModel

class AlbumModel(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(null=True)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE, null=True, blank=True,related_name='albums')

    def __str__(self):
        return self.name
