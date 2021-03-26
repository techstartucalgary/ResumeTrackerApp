from rest_framework import serializers
from . models import *
import PyPDF2
  

    
class ReactSerializer(serializers.ModelSerializer):
    
    def test_method(self):
        print("Heyyy!")
        q = self.initial_data
        files = q.FILES
        f = files['myFile']
        print(f.size)
        print(files)
        #pdfFileObj = open('testResume.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(f, raise_exception=True)
        pageObj = pdfReader.getPage(0)
        text = pageObj.extractText()
        #print(text)
    
    class Meta:
        model = React
        fields = ['totalScore', 'educationScore', 'educationComments',
        'experienceScore', 'experienceComments', 'formattingScore', 
        'formattingComments', 'name', 'detail']
