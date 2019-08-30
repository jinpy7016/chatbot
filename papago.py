import pprint
import requests
from decouple import config

# 1. 환경 변수 설정

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
print(naver_client_id)

# 2. URL 설정
url = 'https://openapi.naver.com/v1/papago/n2mt'
# 3. 헤더 및 data 설정
headers = {
    'X-Naver-Client-Id' : naver_client_id,
    'X-Naver-Client-Secret' : naver_client_secret
}
data = {
    'source': 'ko',
    'target': 'en',
    'text': '댕댕이'
}
# 4. 요청
response = requests.post(url, headers=headers,data=data).json()
#print(response)
pprint.pprint(response['message']['result']['translatedText'])