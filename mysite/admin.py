from django.contrib import admin
from mysite.models import CompanyType, News,Company,StockInfo

admin.site.register(News)
admin.site.register(Company)
admin.site.register(StockInfo)
admin.site.register(CompanyType)