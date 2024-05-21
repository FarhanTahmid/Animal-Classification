from django.shortcuts import render,redirect
from . models import *
from . classifier import *
from django.http import JsonResponse
# Create your views here.

def homepage(request):
    return render(request,'index.html')

def classificationPage(request):
    context={
            
    } 
    if(request.method=="POST"):
        image_file=request.FILES.get('animal_image')
        prediction=Classifier.predict_class(image_path=image_file)
        context={
            'prediction':prediction.upper,
        }
    return render(request,'classification.html',context)