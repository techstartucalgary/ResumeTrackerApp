from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
import operator
import fitz  # this is pymupdf
from . Parser import *
import json 

# Create your views here.
  
class ReactView(APIView):
    
    serializer_class = ReactSerializer
  
#     def get(self, request):
#         detail = [ {"name": detail.name,"detail": detail.detail} 
#         for detail in React.objects.all()]
#         return Response(detail)
  
  	# Must implement error checking
    def post(self, request):
        doc = handleRequest(request)
        endData = compute(doc)
        print(endData)
        return Response(endData)



#Must implement an exception handling here if file is not valid 
def handleRequest(request):
	files = request.FILES
	f = files['myFile']
	strm = f.read()
	doc = fitz.open(stream=strm, filetype="pdf")
	#pdfReader = PyPDF2.PdfFileReader(f)
	return doc
	
	
	