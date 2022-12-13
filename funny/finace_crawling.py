from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import requests
from summa.summarizer import summarize
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# pip install pandas
# pip install tabulate
# pip install beautifulsoup4
# pip install lxml
# pip install requests
# pip install summa
# pip install selenium
# pip install webdriver-manager

URL = 'https://finance.naver.com/'
raw = requests.get(URL)
html = BeautifulSoup(raw.text,'lxml')

units_up =  html.select('#_topItems2>tr')  # 금일 최고 상승 종목 다 가져오기

top_item = dict()
top_item["순위"] = []
top_item["이름"] = []
top_item["가격"] = []
top_item["변동가"] = []
top_item["변동률"] = []

print('=================================금일 최고 상승 종목=================================')
print()

i = 1
for unit in units_up:
    title_up = unit.select_one('#_topItems2 > tr> th > a').text
    price_up = unit.select_one('#_topItems2 > tr> td')
    up = unit.select_one('#_topItems2 > tr > td:nth-child(3)').text
    percent_up = unit.select_one('#_topItems2 > tr> td:nth-child(4)')
    up = up.replace('상한가', "")
    up = up.replace('상승', "")
    top_item["순위"].append(i)
    i += 1
    top_item["이름"].append(title_up)
    top_item["가격"].append(price_up.text)
    top_item["변동가"].append("+"+up)
    top_item["변동률"].append(percent_up.text)

top = pd.DataFrame(top_item, columns=["이름", "가격", "변동가", "변동률"], index=top_item["순위"])

print(tabulate(top, headers='keys', tablefmt='psql'))

units_up =  html.select("#_topItems1 > tr") # 금일 인기 종목 다 가져오기

pop_item = dict()
pop_item["순위"] = []
pop_item["이름"] = []
pop_item["가격"] = []
pop_item["변동가"] = []
pop_item["변동률"] = []

print('==================================금일 인기 종목==================================')

i = 1
for unit in units_up:
    title_up = unit.select_one('#_topItems1 > tr> th > a').text
    price_up = unit.select_one('#_topItems1 > tr> td')
    up = unit.select_one('#_topItems1 > tr > td:nth-child(3)').text
    percent_up = unit.select_one('#_topItems1 > tr> td:nth-child(4)')
    
    if percent_up.text[2] == "+":
        up = up.replace('상승', "")
        pop_item["변동가"].append("+" + up)
    elif percent_up.text[2] == "-":
        up = up.replace('하락', "")
        pop_item["변동가"].append("-" + up)
    else:
        up = up.replace('보합', "0")
        pop_item["변동가"].append(up)
    pop_item["순위"].append(i)
    i += 1
    pop_item["이름"].append(title_up)
    pop_item["가격"].append(price_up.text)
    pop_item["변동률"].append(percent_up.text)

pop = pd.DataFrame(pop_item, columns=["이름", "가격", "변동가", "변동률"], index=pop_item["순위"])

print(tabulate(pop, headers='keys', tablefmt='psql'))

# 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

def makeUrl(search, start_pg, end_pg):
    urls = []
    for i in range(start_pg, end_pg + 1):
        page = i
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
        urls.append(url)
    return urls

##########뉴스크롤링 시작###################

print("최고 상승 : 1")
print("인기 : 2")
num = int(input("검색하고 싶은 종목을 선택해주세요. : "))


if num == 1:
    print('=================================금일 최고 상승 종목=================================')
    print(tabulate(top, headers='keys', tablefmt='psql'))
    rank = int(input("검색하고 싶은 종목의 순위를 입력해주세요 : "))
    print(top_item["이름"][rank - 1])
    search = top_item["이름"][rank - 1]
elif num == 2:
    print('=================================금일 인기 종목=================================')
    print(tabulate(pop, headers='keys', tablefmt='psql'))
    rank = int(input("검색하고 싶은 종목의 순위를 입력해주세요 : "))
    print(pop_item["이름"][rank - 1])
    search = pop_item["이름"][rank - 1]

search_urls = makeUrl(search, 1, 2)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)

naver_urls = []
break_index = 0

for i in search_urls:
    driver.get(i)
    time.sleep(1)

    a = driver.find_elements(By.CSS_SELECTOR, 'a.info')
    for i in a:
        i.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)  
        url = driver.current_url
        if "news.naver.com" in url:
            naver_urls.append(url)
        else:
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        break_index += 1
        if break_index > 7:
            break

# ConnectionError방지
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

for i in naver_urls:
    original_html = requests.get(i, headers=headers)
    html = BeautifulSoup(original_html.text, "html.parser")

    # 뉴스 제목 가져오기
    title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
    # list합치기
    title = ''.join(str(title))
    # html태그제거
    pattern1 = '<[^>]*>'
    title = re.sub(pattern=pattern1, repl='', string=title)

    content = html.select("div#dic_area")
    # list합치기
    content = ''.join(str(content))

    # html태그제거 및 텍스트 다듬기
    content = re.sub(pattern=pattern1, repl='', string=content)
    pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
    content = content.replace(pattern2, '')
    
    print("제목")
    print()
    print(title[1:-1])
    print()
    print("본문 요약")
    print()
    print(summarize(content))
    print()