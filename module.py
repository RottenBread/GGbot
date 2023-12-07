import requests
from bs4 import BeautifulSoup

def url(name):
    name = name.replace('#', '-')
    name = name.replace(' ', '%20')
    url = 'https://www.op.gg/summoners/kr/'+name
    hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0')}
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def url2(name):
    name = name.replace('#', '-')
    name = name.replace(' ', '%20')
    url = 'https://fow.kr/find/'+name
    hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0')}
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getGG_solotier(name):
    solorank = url(name).find('div', attrs={"class":"css-1kw4425 ecc8cxr0"})
    solorank_tier = solorank.find('div', attrs={"class":"tier"})
    return solorank_tier

def getGG_flextier(name):
    flexrank = url(name).find('div', attrs={"class":"css-1ialdhq ecc8cxr0"})
    flexrank_tier = flexrank.find('div', attrs={"class":"tier"})
    return flexrank_tier

def getGG_sololp(name):
    solorank = url(name).find('div', attrs={"class":"css-1kw4425 ecc8cxr0"})
    solorank_lp = solorank.find('div', attrs={"class":"lp"})
    return solorank_lp

def getGG_flexlp(name):
    flexrank = url(name).find('div', attrs={"class":"css-1ialdhq ecc8cxr0"})
    flexrank_lp = flexrank.find('div', attrs={"class":"lp"})
    return flexrank_lp

def getGG_solowr(name):
    solorank = url(name).find('div', attrs={"class":"css-1kw4425 ecc8cxr0"})
    solorank_wr = solorank.find('div', attrs={"class":"ratio"})
    return solorank_wr

def getGG_flexwr(name):
    flexrank = url(name).find('div', attrs={"class":"css-1ialdhq ecc8cxr0"})
    flexrank_wr = flexrank.find('div', attrs={"class":"ratio"})
    return flexrank_wr

def getGG_solowl(name):
    solorank = url(name).find('div', attrs={"class":"css-1kw4425 ecc8cxr0"})
    solorank_wl = solorank.find('div', attrs={"class":"win-lose"})
    return solorank_wl

def getGG_flexwl(name):
    flexrank = url(name).find('div', attrs={"class":"css-1ialdhq ecc8cxr0"})
    flexrank_wl = flexrank.find('div', attrs={"class":"win-lose"})
    return flexrank_wl

def getFOW_recent_win(name):
    recent = url2(name).find('td', attrs={"class":"recent_td"})
    return recent

def getFOW_recent(name):
    recent = url2(name).find('table', attrs={"class":"tablesorter table_recent"})
    recent_game = recent.find('b')
    return recent_game

def getFOW_recent_avg(name):
    recent = url2(name).find('table', attrs={"class":"tablesorter table_recent"})
    recent_game_avg = recent.find('u')
    return recent_game_avg

def remove_after_char(input_str, char):
    parts = input_str.split(char)
    result = parts[0]

    return result
