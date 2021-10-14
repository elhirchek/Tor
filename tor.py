import sys,requests,subprocess
from rich import print
from bs4 import BeautifulSoup as bs

#Website

class WebSite:
    
    def __init__(self,url:str = None,name:str = None):
        
        self.url = f"{url}{name}"
        self.names = []
        self.info = []
        self.num:int = None
        
    def soup_(self):

        res = requests.get(f"{self.url}").content
        self.soup = bs(res,'html.parser') 
        return self.soup

    def prin_t(self,n:int):

        j =int(0)
        for x,i in enumerate(self.names):
            print(f"[blue]{x} ==> {i.string}[/blue]") 
            while j != "t":
                print(self.info[j:j+n])
                j+=n
                break
    
    def scend_soup(self,s_url):

        scend_res = requests.get(f"{s_url}{self.names[self.num].get('href')}").content
        scend_soup = bs(scend_res,'html.parser')
        self.magnet = [i.get('href') for i in scend_soup.find_all('a',href=True) if str(i.get('href')).startswith('magnet')]
        return self.magnet

    def stream(self):
        
        subprocess.run([f"peerflix -a --mpv -r \"{self.magnet[0]}\""],shell=True)
    
    # def download(self):
    #     subprocces.run(['aria2c',f'{self.mag()}'],shell=True)

#Website

#help

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

#help

#rarbg

if "-r" in sys.argv:

    rarbg = WebSite("https://rarbg.unblockninja.com/search/?search=",f"{sys.argv[-1]}")
    rarbg.soup_()
    rarbg.names = [i for i in rarbg.soup.find_all("a",href=True,title=True) if not str(i.text).startswith("\n")]
    rarbg.info = [i.text for i in rarbg.soup.find_all('td',class_='lista') if not str(i.text).startswith('\n')]
    rarbg.prin_t(6)
    rarbg.num = int(input("enter the number:")) 
    rarbg.scend_soup("https://rarbg.unblockninja.com")
    if "-m" in sys.argv:
        print(f"[blue]{rarbg.magnet[0]}[/blue]")
    elif "-s" in sys.argv:
        rarbg.stream()

#rarbg
#nyaa.si

if "-n" in sys.argv:

    nyaa = WebSite("https://nyaa.si/?f=0&c=0_0&q=",f"{sys.argv[-1]}")
    nyaa.soup_()
    nyaa.names = [i for i in nyaa.soup.find_all("a",title=True) if not str(i.text).startswith('\n')] 
    nyaa.info = [i.text for i in nyaa.soup.find_all('td',class_='text-center') if not str(i.text).startswith('\n')]
    nyaa.prin_t(5)
    nyaa.num = int(input("enter the number:"))
    nyaa.scend_soup("https://nyaa.si")
    if "-m" in sys.argv:
        print(f"[blue]{nyaa.magnet[0]}[/blue]")
    elif "-s" in sys.argv:
        nyaa.stream()

#nyaa.si

#torrentGalaxy

if "-t" in sys.argv:
    
    torrent_galaxy = WebSite("https://torrentgalaxy.to/torrents.php?search=",f"{sys.argv[-1]}")
    torrent_galaxy.soup_()
    torrent_galaxy.names = [i for i in torrent_galaxy.soup.find_all('a',title=True,class_='txlight') if not re.match(r'\d',str(i.text))]
    torrent_galaxy.info = [i.text for i in torrent_galaxy.soup.find_all('div',class_="tgxtablecell collapsehide rounded txlight") if not str(i.text).startswith('\n') and str(i.text) != '-' and str(i.text) != '']
    torrent_galaxy.prin_t(5)
    torrent_galaxy.num = int(input("enter the number:"))
    torrent_galaxy.scend_soup("https://torrentgalaxy.to")
    if "-m" in sys.argv:
        print(f"[blue]{torrent_galaxy.magnet[0]}[/blue]")
    elif "-s" in sys.argv:
        torrent_galaxy.stream()
    
#torrentGalaxy
