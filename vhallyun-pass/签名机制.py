import time
import hashlib #加密算法
import requests

signed_at = str(round(time.time()))  #time.time()返回当前时间的时间戳    round返回浮点的四舍五入值round(x,2)
# signed_at = '1568778046'
print(signed_at)

secretkey = '475de36de482e9a2da9813dc2bd91a0d'
params = {'app_id':'aa32fd92','signed_at':signed_at,'room_id':'lss_bd9a20f5'}
sort_list = sorted(params.keys()) #对键进行排序,已列表形式返回

result = secretkey
for key in sort_list:
    result = result+key+params[key]
result = result+secretkey
print(result)

sign = hashlib.md5(result.encode(encoding='utf-8')).hexdigest() #可以转为UTF-8、GBK、GB2312、GB18030

print(sign)

params['sign'] = sign
response = requests.get('http://t-open.e.vhall.com/api/v1/room/disable',params=params)
print(response.json())