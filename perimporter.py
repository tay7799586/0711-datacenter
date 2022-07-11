# import json
# import requests
# import django, os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
# django.setup()

# a=requests.get("https://www.twse.com.tw/exchangeReport/BWIBBU?response=json&date=20220501&stockNo=2330")
# b=a.json()
# print(b["fields"][0],b["fields"][3], b["fields"][4])

# for c in b['data']:
#     print(c[0],c[3],c[4])