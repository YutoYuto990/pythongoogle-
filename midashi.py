import requests
from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
def searc(kwargs,num):
    search_word = kwargs

# how many content
    pages_num=num

    print(f'【word】{search_word}')

# Google page
    url = f'https://www.google.co.jp/search?hl=ja&num={pages_num}&q={search_word}'
    request = requests.get(url)
    listb=[]
# Google page html
    soup = BeautifulSoup(request.text, "html.parser")
    search_site_list = soup.select('div.kCrYT > a')
    for rank, site in zip(range(1, pages_num), search_site_list):
        try:
            site_title = site.select('h3.zBAuLc')[0].text
        
        except IndexError:
            site_title = site.select('img')[0]['alt']
        site_url = site['href'].replace('/url?q=', '')
        q=site_url.find("&sa")
    # result
        result=f"[{site_title}]({unquote(site_url[:q])})"
    
    #urldecode
    
        res=unquote(f"{result[:q]})")
        rem=requests.get(unquote(site_url[:q]))
        be=BeautifulSoup(rem.text,"html.parser")
        h1s=be.find("h2")
        try:
          if "<span" or "<a" not in str(h1s):
            listb.append(f"{result}\n{h1s.text}\n")
          else:
            h2s=be.find("h1")
            if "<a " or "<span"not in str(h2s):
                listb.append(f"{result}\n{h2s.text}\n")
            else:
                h3s=be.find("title")
                listb.append(f"{result}\n{h3s.text}\n")
        except:
          listb.append(f"{result}\nこのページの情報はありません\n")
    return listb
