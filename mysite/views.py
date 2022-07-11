from django.shortcuts import render
from mysite.models import Company, CompanyType, News, StockInfo
import random

def index(request):
    name= "News Information"
    news=News.objects.all()
    return render(request, "index.html", locals())

def lotto(request):
    lotto = [i for i in range(1,50)]
    random.shuffle(lotto)
    lotto = lotto[:6]
    return render(request, "lotto.html", locals())

def show(request, id):
    item= News.objects.get(id=id)
    return render(request, "show.html" , locals())

def stock(request):
    ct = CompanyType.objects.all()
    return render(request, "stock.html", locals())

def company(request, id):
    ct = CompanyType.objects.get(id=id)
    companies = Company.objects.filter(ct=ct)
    return render(request, "company.html", locals())

def stockinfo(request, id):
    company= Company.objects.get(id=id)
    data = StockInfo.objects.filter(company=company)
    return render(request, "stockinfo.html", locals())