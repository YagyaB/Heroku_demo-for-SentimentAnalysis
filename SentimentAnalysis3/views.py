from django.http import HttpResponse
from django.shortcuts import render
import joblib
#from sklearn.feature_extraction.text import CountVectorizer 
#cv = CountVectorizer()
#from sklearn.feature_extraction.text import TfidfTransformer
#tfidf_transformer = TfidfTransformer()
#training_data = cv.fit_transform(X_train)
#Xtrain_tfidf = tfidf_transformer.fit_transform(training_data)

def home(request):
    return render(request,"home.html")

def result(request):

    P = joblib.load('finalized_model3.sav')

    lis = []

    lis.append(request.GET['comment'])

    #doc = ['This product so far has not disappointed', 'electronics product are bad']
    #doc_counts = cv.transform(doc)
    #lis_counts = cv.transform(lis)
    #doc_tfidf=tfidf_transformer.transform(doc_counts)
    #lis_tfidf = tfidf_transformer.transform(lis_counts)
    #predicted= LR.predict(doc_tfidf)

    answer = P.predict(lis)
    #answer = LR.predict(lis_tfidf)

    return render(request,"result.html",{'answer':answer})    

   