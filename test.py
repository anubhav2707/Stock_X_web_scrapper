import csv
import json
import requests

header = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36" ,'referer':'https://www.google.com/',
  "upgrade-insecure-requests":"1",
  "sec-fetch-site": "cross-site",
  "sec-ch-ua": 'Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86',

  }

filename = "stockx.csv"
csvfile =  open(filename, 'w')   
csvwriter = csv.writer(csvfile)

for i in range (25):
    url = "https://stockx.com/api/browse?productCategory=sneakers&page="+str(i+1)
    print(url)
    htmlContent = requests.get(url, headers=header)
    data = htmlContent.text
    jsonObj = json.loads(data)
    product=jsonObj['Products']
 
    csvwriter.writerow(["id","uuid","Brand","Name","Description","ColorWay","Country of Manufacture","gender","Retail Price","Release date","Release Time","Below Retail","image small","Tags","Name","Shoe","Short Description","Ticker Symbol","Style Id"])
    for product_data in product:
        title=product_data['title']
        description=product_data['description']

        csvwriter.writerow([product_data['id'],product_data['uuid'],product_data['brand'],product_data['title'],product_data['description'],product_data['colorway'],product_data['countryOfManufacture'],product_data['gender'],product_data['retailPrice'],product_data['releaseDate'],product_data['releaseTime'],product_data['belowRetail'],product_data['media'],product_data['_tags'],product_data['name'],product_data['shoe'],product_data['shortDescription'],product_data['tickerSymbol'],product_data['styleId']])