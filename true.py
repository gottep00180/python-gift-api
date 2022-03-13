import requests
import json
phone = "YourPhonHereBro"
voucher_hash = "ajAmD2nTVpvdmjflqg"
url = 'https://gift.truemoney.com/campaign/vouchers/'+str(voucher_hash)+'/redeem'
x = requests.post(url,
json={"mobile" : phone , "voucher_hash" : voucher_hash},
headers={
    "Accept": "application/json",
    "content-type" : "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "https://gift.truemoney.com",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    }
)
print(x.text)
#คือมันก็แค่การเพิ่ม user-agent การ patch รอบหน้าอาจจะแตกจริงๆ
