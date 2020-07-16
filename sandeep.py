import requests
from bs4 import BeautifulSoup

mypage = requests.get(
    "https://www.amazon.in/dp/B003LSOH8E/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B003LSOH8E&pd_rd_w=pErvt&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=yURei&pf_rd_r=15TPNJC7YWV3ZG58P14J&pd_rd_r=f9d3ba1a-0d7b-4f3d-b9ba-1c8692ef00d4&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOVo3TkpXSkRIVFYzJmVuY3J5cHRlZElkPUEwNTA1MzgxMzg1OVg3WkExRUpRQiZlbmNyeXB0ZWRBZElkPUEwMzI3NjUwMVpKOEJJWVJINkROSCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
soup = BeautifulSoup(markup=mypage.text, features="html.parser")
price = soup.find("span", {'id': 'priceblock_ourprice'})
print("amazon price")
print(price.text)
