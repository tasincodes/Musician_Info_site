from django.db import models

class Musician(models.Model):
    id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=20)
    instrument = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.First_name + " " + self.Last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating_tuple = (
        (1,"best"),(2,"medium"),
        (3,"worst")
    )
    rating = models.IntegerField(choices=rating_tuple)

    def __str__(self) -> str:
        return self.name +" Rating :"+ str(self.rating)