# coding:utf-8
from common import get_parameter

import requests
import json
url = "http://202.97.158.140:10035/BaseInfo/QueryBaseVehInfoData"
cars =[]
lastdata = []

para = get_parameter.Data(r"E:\autotest\datas\Shanxi_01.xls","Sheet1")
car = para.get_data()

for i in range(1,len(car)+1):
     cars.append(car[i]["车牌号码"])

for i in range(len(cars)):
    datas = {
    "Model": """{{"LicensePlat":"{}","ZoneName":"山西省","ZoneId":"14000000","UnitId":"0","PlatformName":"","PlatformId":"0","CarType":0,"GpsInstalled":-1,"Status":0,"GovStatus":2,"ProviderName":"","ProviderId":"0","UserId":"25","PageIndex":1,"PageSize":10,"IsSplitPage":"true","TotalIndex":-1}}""".format(cars[i])
    }
    headers={
        "Cookie": "ASP.NET_SessionId=4upt0rakrgcmy0fappm21dym; JiaoJingGOV=1B08DEF58D86B90F0DB9AE7A5AD21A9F187ED1A8A620134EA3ABE22170A298D7778C58B3D2350A0499B75CF1478A64BCDA41F6AE0457AE430958B02E4BB995F8FD622BA1409A637884EF2181A3F9EC18C15283B553E11EA46BED4892A3814F2C7448A8DAA8A1005F975DC7A8A5124145AEFD7078D77B78D7EB80CC8355DBA18075E3B9E9AD94FA59584551830B5758E9; SessionFn=DC3F6A56A3CF80896AAFC6284380C483-1784169002"
    }
    re = requests.post(url,datas,headers=headers)
    cardata = re.json()
    #print(cardata)
    if json.loads(cardata["retVal"])["aaData"]:
        last = json.loads(cardata["retVal"])["aaData"][0]["GPSLastDate"]
        print(last)
        lastdata.append(last)
    else:
        print("无数据")
print(lastdata)