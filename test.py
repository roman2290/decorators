import requests
from bs4 import BeautifulSoup
import bs4
from fake_headers import Headers
from main import logger
import os
import json




@logger
def get_link():
    fake_head = Headers(browser="opera", os="win").generate()
    return fake_head

def get_head():
    response = requests.get("https://spb.hh.ru/search/vacancy",
                         headers=get_link())
    main_page_data = bs4.BeautifulSoup(response.text, features="lxml")
    main = main_page_data.find("main", class_ = "vacancy-serp-content")
    v_card = main.find_all("div", class_= "vacancy-search-item__card")
    return get_head(v_card)

def my_job(v_card):
    list_vacance = []
    for job_h in v_card:
    
        salary_s = job_h.find("div", class_ = "narrow-container--lKMghVwoLUtnGdJIrpW4").find("span", class_ = "bloko-text")
        salary = salary_s
    
        name_company = job_h.find(class_ = "bloko-link bloko-link_kind-secondary")
        company = name_company.text.strip()

        city = job_h.find("div", class_ = "narrow-container--lKMghVwoLUtnGdJIrpW4").find("span", class_ = "bloko-text")
        city_c = city

        link_job = job_h.find("a", attrs = {"data-qa": "vacancy-serp__vacancy-employer"})
        site_link_job = link_job["href"]
        link_site = f'https://spb.hh.ru/search/vacancy{site_link_job}'

        list_job = ({
        'salary': salary,
        'company': company,
        'city_c':city_c,
        'link_site': link_site
    })
    list_vacance.append(list_job)



def test_3():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'




if __name__ == '__main__':
    test_3()