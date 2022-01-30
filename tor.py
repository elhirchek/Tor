# Standard Library
import sys
import subprocess
import re

# Third Party Library
import requests
from rich import print
from bs4 import BeautifulSoup as bs

# Website

class WebSite:
    
    def __init__(self,url:str = None,name:str = None):
        
        self.url = f"{url}{name}"
        self.s_url = f"{url}"
        self.names = []
        self.info = []
        self.num:int = None
        
    def soup_(self,parmter:str = None):

        if parmter == 'scend':
            self.soup = bs(requests.get(f"{self.s_url}{self.names[self.num].get('href')}").content,'html.parser') 
            return self.soup
        elif parmter:
            self.soup = bs(requests.get(f"{self.url}",params={parmter:sys.argv[-1]}).content,'html.parser')
            return self.soup
        else:
            self.soup = bs(requests.get(f"{self.url}").content,'html.parser') 
            return self.soup

    def check_resault(self):

        if self.names:
            pass
        else:
            print('No results were returned. Please refine your search.')
            sys.exit(0)

    def prin_t(self,n:int = None,eztv = None):

        if eztv:
            j = int(17)
        else:
            j = int(0)

        for x,i in enumerate(self.names):

            # Print Names
            if eztv:
                print(f"[blue]{x} ==> {i.get('title')}[/blue]") 
            else:
                print(f"[blue]{x} ==> {i.text}[/blue]") 

            # Print Info
            if self.info and eztv:
                print(self.info[j:j+n])
                j+=6
                continue
            elif self.info:
                print(self.info[j:j+n])
                j+=n
                continue
            else:
                continue

    def scend_soup(self):

        scend_res = requests.get(f"{self.s_url}{self.names[self.num].get('href')}").content
        scend_soup = bs(scend_res,'html.parser')
        self.magnet = [i.get('href') for i in scend_soup.find_all('a',href=True) if str(i.get('href')).startswith('magnet')]
        return self.magnet

    def stream(self):
        
        subprocess.run([f"peerflix -a --mpv -r \"{self.magnet[0]}\""],shell=True)
    
    # def download(self):
    #     subprocces.run(['aria2c',f'{self.mag()}'],shell=True)

# Website

# Check for reqiurment
# help

if sys.argv[-1] == "-h" or sys.argv[-1] == "--help" or len(sys.argv) == 1:
    print(
       """
Tor
    *usage:
    tor website options names

    *website:
    -n --> nyaa.si
    -t --> torrentGalaxy
    -r --> rarbg
    -e --> eztv
    -x --> 1337x

    *options:
    -s --> for stream using mpv and webtorrent
    -m --> return magnet_link
    -d --> downlaod torrent using aria2 //still not working

    *ex:
    tor -n -s attack.on.titan
    tor -t -s game.of.thrones
"""
)
    sys.exit()

# help

# rarbg

if "-r" in sys.argv:

    rarbg = WebSite("https://rarbg.unblockninja.com",f"/search/?search={sys.argv[-1]}")
    rarbg.soup_()
    rarbg.names = [i for i in rarbg.soup.find_all("a",href=True,title=True) if not str(i.text).startswith("\n")]
    rarbg.check_resault()
    rarbg.info = [i.text for i in rarbg.soup.find_all('td',class_='lista') if not str(i.text).startswith('\n')]
    rarbg.prin_t(6)
    rarbg.num = int(input("enter the number:")) 
    rarbg.scend_soup()
    if "-m" in sys.argv:
        print(f"[blue]{rarbg.magnet[0]}[/blue]")
    elif "-s" in sys.argv:
        rarbg.stream()

# rarbg

# nyaa.si

if "-n" in sys.argv:

    nyaa = WebSite("https://nyaa.si",f"/?f=0&c=0_0&q={sys.argv[-1]}")
    nyaa.soup_()
    nyaa.names = [i for i in nyaa.soup.find_all("a",title=True) if not str(i.text).startswith('\n')] 
    nyaa.check_resault()
    nyaa.info = [i.text for i in nyaa.soup.find_all('td',class_='text-center') if not str(i.text).startswith('\n')]
    nyaa.prin_t(5)
    nyaa.num = int(input("enter the number:"))
    nyaa.scend_soup()
    if "-m" in sys.argv:
        print(f"[blue]{nyaa.magnet[0]}[/blue]")
    elif "-s" in sys.argv:
        nyaa.stream()

# nyaa.si

# torrentGalaxy

if "-t" in sys.argv:
    
    torrent_galaxy = WebSite("https://torrentgalaxy.to",f"/torrents.php?search={sys.argv[-1]}")
    torrent_galaxy.soup_()
    torrent_galaxy.names = [i for i in torrent_galaxy.soup.find_all('a',title=True,class_='txlight') if not re.match(r'\d',str(i.text))]
    torrent_galaxy.check_resault()
    torrent_galaxy.info = [i.text for i in torrent_galaxy.soup.find_all('div',class_="tgxtablecell collapsehide rounded txlight") if not str(i.text).startswith('\n') and str(i.text) != '-' and str(i.text) != '']
    torrent_galaxy.prin_t(5)
    torrent_galaxy.num = int(input("enter the number:"))
    torrent_galaxy.scend_soup()
    if "-m" in sys.argv:
        print(f"[blue]{torrent_galaxy.magnet[0]}[/blue]")
    elif "-s" in sys.argv:
        torrent_galaxy.stream()
    
# torrentGalaxy

# eztv
if '-e' in sys.argv:

    eztv = WebSite("https://eztv.re",f"/search/{sys.argv[-1]}")
    eztv.soup_()
    eztv.names = [i for i in eztv.soup.find_all('a',href=True,title=True,class_='magnet')]
    eztv.check_resault()
    eztv.info = [i.text for i in eztv.soup.find_all('td')]
    eztv.prin_t(3,True)
    eztv.num = int(input("enter the number:"))
    if "-m" in sys.argv:
        print(f"[blue]{eztv.names[eztv.num].get('href')}[/blue]")
    if "-s" in sys.argv:
        eztv.stream()

# 1337x

if "-x" in sys.argv:

    _1337x = WebSite("https://1337x.wtf",f"/search/{sys.argv[-1]}/1/")
    _1337x.soup_()
    _1337x.names = [i for i in _1337x.soup.find_all("a",href=True) if str(i.get('href')).startswith('/torrent')] 
    _1337x.check_resault()
    _1337x.info = [i.text for i in _1337x.soup.find_all('td',class_=True) if str(i.get('class')[0]) != "coll-1"]
    _1337x.prin_t(5)
    _1337x.num = int(input("enter the number:"))
    _1337x.scend_soup()
    if "-m" in sys.argv:
        print(f"[blue]{_1337x.magnet[0]}[/blue]")
    elif "-s" in sys.argv:
        _1337x.stream()

# Subscene

#if "-S" in sys.argv:
#
#    sub = WebSite('https://subscene.com','/subtitles/searchbytitle')
#    sub.soup_('query')
#    sub.names = [i for i in sub.soup.find_all('a',href=True) if str(i.get('href')).startswith('/subtitles') ]
#    sub.check_resault()
#    sub.prin_t()
#    sub.num = int(input("enter the number:"))
#    sub.soup_('scend')
#    sub.names = [i for i in sub.soup.find_all('a',href=True) if str(i.get('href')).startswith('/subtitles') ]
#    #lang = [i.span.text[8:i.span.text.index(re.search(r'\w\r\n',i.span.text).group())+1] for i in sub.names ]
#    #name = [i.span.find_next_sibling('span').text[8:i.span.find_next_sibling('span').text.index(re.search(r'\w \r\n',i.span.find_next_sibling('span').text).group())+1] for i in sub.names]
#    #g = sub.names[0].span.find_next_sibling('span').text
#    #name = g[8:g.index(re.search(r'\w\r\n',g).group())+1]
#    print(repr(sub.names))
#    #name = re.search(r'\w \r\n',g)
#    print(name)
#    #for i in sub.names:print(i.span.text.index('e\r\n\t\t\t\t'))
#    #for i in sub.names:print(i.span.text[8:i.span.text.index('e\r')])
#    #for i in sub.names:print(i.span.text[8:i.span.text.index(r'\r')],"-->",i.span.find_next('span').text[i.span.text.index(r'\r\n\t\t\t\t\t\t'):i.span.find_next('span').text.index(r'\r')])
#    #'\n\r\n\t\t\t\t\t\tBurmese\r\n\t\t\t\t\t\n\r\n\t\t\t\t\t\tWho Is Sinner? Sung by SOPA Students \r\n\t\t\t\t\t\n'
#
## Func Mian
#
#def main():
#    pass
