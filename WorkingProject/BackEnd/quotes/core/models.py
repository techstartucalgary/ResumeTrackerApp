from django.db import models
import PyPDF2
  
# Create your models here.
  
  
class React(models.Model):
    totalScore = models.CharField(max_length = 5)
    educationScore = models.CharField(max_length = 5)
    educationComments = models.CharField(max_length = 500)
    experienceScore = models.CharField(max_length = 5)
    experienceComments = models.CharField(max_length = 500)
    formattingScore = models.CharField(max_length = 5)
    formattingComments = models.CharField(max_length = 500)
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)



	