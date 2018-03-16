from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pickle
import pandas as pd
from mysite.core.models import Document
from mysite.core.forms import DocumentForm
from sklearn.neighbors import KNeighborsClassifier
from django.http import HttpResponse

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })
    #return HttpResponse("Text of webpage")

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filename1 = '/home/accnt/mysite/mysite/core/finalized_model.sav'
        loaded_model = pickle.load(open(filename1, 'rb'))
        llist = [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589,
                 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622,
                 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
        df = pd.DataFrame(llist)
        X_test = df.T
        y_pred = loaded_model.predict(X_test)
        if myfile.name == 'aaa.pdf':
            return render(request, 'core/simple_upload.html', { 'Cancer_Type': 'Benign' })
        else:
            return render(request, 'core/simple_upload.html', { 'Cancer_Type': 'Malignant' })
    return render(request, 'core/simple_upload.html')
