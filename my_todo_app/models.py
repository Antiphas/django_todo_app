from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class StaffBiodata(models.Model):
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname




