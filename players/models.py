from django.db import models

class Team(models.Model):
    
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    rating = models.IntegerField()
    team = models.ForeignKey(Category, on_delete=models.CASCADE)  def __str__(self):
    
    return self.name +" - "+str(self.age)
