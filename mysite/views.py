from django.shortcuts import render
import random

def index(request):
    name= "Meine Dammen und Herren"
    
    return render(request, "index.html", locals())

def lotto(request):
    lotto = [i for i in range(1,50)]
    random.shuffle(lotto)
    lotto = lotto[:6]
    return render(request, "lotto.html", locals())