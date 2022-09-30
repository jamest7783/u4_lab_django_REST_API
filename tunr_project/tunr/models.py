from django.db import models

class Team(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    division=models.CharField(max_length=100)
    wins=models.IntegerField()
    losses=models.IntegerField()

    def __str__(self):
        return self.name

class Player(models.Model):
    team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    first_name=models.CharField(max_length=100,default='first name')
    last_name=models.CharField(max_length=100,default='last name')
    position=models.CharField(max_length=100)
    age=models.IntegerField()
    injured=models.BooleanField()

    def __str__(self):
        return self.first_name+' '+self.last_name


