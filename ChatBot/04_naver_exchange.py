# 0. 관련 모듈 import
import requests
from bs4 import BeautifulSoup
# 네이버금융-시장지표-원달러 환율 가져오기
# 1. 페이지에 요청을 보내서 HTML 문서를 문자열 형태로 가져온다.
url = "https://finance.naver.com/marketindex/"
html = requests.get(url).text
# 2. HTML 문서에서 손쉽게 데이터를 가져오기 위해 BeautifulSoup 클래스 객체를 받아온다.
soup = BeautifulSoup(html,'html.parser')
# 3. 가져올 태그의 선택자를 넣고 결과물을 가져온다.
USD = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").text
# 4. 결과물 출력
print(USD)


