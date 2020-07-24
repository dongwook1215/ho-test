from django.db import models

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=17)
    date = models.DateTimeField('날짜를 입력해주세요.')
    text = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:50]
