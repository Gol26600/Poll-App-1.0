from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=250)
    option1 = models.CharField(max_length=100, verbose_name="Option 1:")
    option2 = models.CharField(max_length=100, verbose_name="Option 2:")
    option3 = models.CharField(max_length=100, verbose_name="Option 3:")
    option4 = models.CharField(max_length=100, verbose_name="Option 4:")
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)
    option4_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.question)
