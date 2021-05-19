from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def start(request):
    end_point = 'https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/alma-ata/'
    # end_point = 'https://www.olx.kz/transport/moto/alma-ata/'
    temp = requests.get(end_point)
    # print(dir(temp))
    # print('Status', temp.status_code)
    # print('Content', temp.content)

    if temp.status_code == 200:
        olx_main = BeautifulSoup(temp.content, 'html.parser')
        # title = olx_main.select('.maincategories h3')
        # title = olx_main.select('.footer-business-partner__slogan strong')
        # title = olx_main.select('.c73.marginbott5')
        page = olx_main.select('.block.br3.brc8.large.tdnone.lheight24 span')
        last_page = int(page[-1].text)
        urls = []
        
        for i in range(1, last_page + 1):
            urls.append(f'{end_point}?page={i}')

        for parse_endpoint in urls:
            current_page = requests.get(parse_endpoint)
            content = BeautifulSoup(current_page.content, 'html.parser')
            offer_title = content.select('.marginright5.link.linkWithHash.detailsLink strong')
            print(offer_title)

    return HttpResponse(page)

"""
     .className - class
     #idName - id
""" 