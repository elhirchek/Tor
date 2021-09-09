import requests,sys,subprocess,re
from bs4 import BeautifulSoup as bs

class WebSite:
    
    def __init__(self,url:str = None,name:str = None):
        
        self.url = f"{url}{name}"
        if name != "None" or name == "-h" or name == "--help":res = requests.get(self.url).content
        self.soup = bs(res,'lxml')
        self.names = []
        self.magnet = []
        self.num:str = None
        
    def mag(self):
        
        if self.magnet == []:
            print("set list comprehension ^_^")
        else:
            return self.magnet[self.num]

    def stream(self):
        subprocess.run(["webtorrent", "--playlist", "--mpv",f'{self.mag()}'],shell=True)
    
    def download(self):
        subprocces.run(['aria2c',f'{self.mag()}'],shell=True)

#help
if sys.argv[-1] == "-h" or sys.argv[-1] == "--help":
           print(
           """tor [website] [options] [names]
           [website]
           -n --> nyaa.si
           -t --> torrentGalaxy
           [options]
           -s --> for stream using mpv and webtorrent
           -m --> return magnet_link
           -d --> downlaod torrent using aria2
           [example]
           tor -n -s attack.on.titan
           tor -t -s game.of.thrones
           """
           )
           sys.exit(0)
#help
#nyaa.si
nyaa = WebSite("https://nyaa.si/?f=0&c=0_0&q=",f"{sys.argv[-1]}")
nyaa.names = [i.text for i in nyaa.soup.find_all("a",title=True) if not str(i.text).startswith('\n')]
nyaa.magnet = [i.get('href') for i in nyaa.soup.find_all('a',href=True) if str(i.get('href')).startswith('mag')]

if "-n" in sys.argv and "-m" in sys.argv:
    for x,i in enumerate(nyaa.names):print(x,"-->",i)
    num = int(input("enter num: "))
    nyaa.num = num
    print(nyaa.mag())

if "-n" in sys.argv and "-s" in sys.argv:
    for x,i in enumerate(nyaa.names):print(x,"-->",i)
    num = int(input("enter num: "))
    nyaa.num = num
    nyaa.stream()
#nyaa.si
#torrentGalaxy
torrent_galaxy = WebSite("https://torrentgalaxy.to/torrents.php?search=",f"{sys.argv[-1]}")
torrent_galaxy.names = [i.text for i in torrent_galaxy.soup.find_all('a',title=True,class_='txlight') if not re.match(r'\d',str(i.text))]
torrent_galaxy.magnet = [i.get('href') for i in torrent_galaxy.soup.find_all('a',href=True) if str(i.get('href')).startswith('magnet')]

if "-t" in sys.argv and "-m" in sys.argv:
    for x,i in enumerate(torrent_galaxy.names):print(x,"-->",i)
    num = int(input("enter num: "))
    torrent_galaxy.num = num
    print(torrent_galaxy.mag())

if "-t" in sys.argv and "-s" in sys.argv:
    for x,i in enumerate(torrent_galaxy.names):print(x,"-->",i)
    num = int(input("enter num: "))
    torrent_galaxy.num = num
    torrent_galaxy.stream()
#torrentGalaxy
