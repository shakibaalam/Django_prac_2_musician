# from django.db import models
# from album.models import AlbumModel

# class MusicianModel(models.Model):
#     f_name = models.CharField(max_length=100)
#     l_name = models.CharField(max_length=100)
#     email=models.EmailField(max_length=100)
#     phone_no=models.CharField(max_length=20)
#     instrument_type=models.CharField(max_length=200)
#     album=models.ForeignKey(AlbumModel,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.f_name + " " + self.l_name

from django.db import models

class MusicianModel(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    instrument_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"