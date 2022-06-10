# Standard Library
import sys
import subprocess
import re
import os
import zipfile
import argparse

# Third Party Library
import requests
from rich import print
from bs4 import BeautifulSoup as bs

# default website

default_website = "1337x"

# Website

class WebSite:
    
    def __init__(self,url:str = None,name:str = None):
        
        self.url = f"{url}{name}"
        self.s_url = f"{url}"
        self.names = []
        self.info = []
        self.soup = None
        self.headers = {
                "User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.2 Chrome/87.0.4280.144 Safari/537.36',
                }
        
    def scrape(self,url):

        request = requests.get(f"{url}",headers=self.headers)
        if request.status_code != 200:print('error in connection try agian');sys.exit(0)
        self.soup = bs(request.content,'html.parser') 
        return self.soup

    def prin_t(self,steps:list[int] = [0,0,0]):

        if not self.names:print('No results were returned. Please refine your search.');sys.exit(0)

        os.system('cls' if os.name == 'nt' else 'clear')
        for x,i in enumerate(self.names):

            # Print Names
            print(f"[blue]{x} ==> {i.text}[/blue]") 

            # Print Info
            if not self.info:continue
            print(f"[green]{self.info[steps[0]:steps[0]+steps[1]]}[/green]")
            steps[0]+=steps[1]+steps[2]

    def magnet(self):

        self.scrape(self.s_url)
        self.magnet = [i.get('href') for i in self.soup.find_all('a',href=True) if str(i.get('href')).startswith('magnet')]
        return self.magnet[0]

    def stream(self,player,streamer):
        
        subprocess.run([f"{streamer} --{player} \"{self.magnet[0]}\""],shell=True)
    
    def download(self):
        subprocess.run([f'aria2c\"{self.magnet[0]}\"'],shell=True)

    # def silent_mode(self):
    #

# help

provider_list = ['nyaa','torrentglaxy','eztv','1337x']
parser = argparse.ArgumentParser(prog='tor',)
# parser.add_argument('-s','--stream',help='start streaming torrent content',action='store_true')
# parser.add_argument('-d',metavar=' ',help='start downloading torrent content',action='store_true')
parser.add_argument('-w',dest='website',metavar='website',default=f"{default_website}",help=f'available website to query from: {provider_list}')
parser.add_argument('name',help='Movie/Anime/Tvshow')
args=parser.parse_args()

# Website

provider = {
        'nyaa': # nyaa
            [
                'https://nyaa.si', #title
                f"/?q={args.name}", # search url
                [
                    {'title':True}, # filter soup based element
                    lambda i: str(i.text).startswith('\n') # filter junk elements
                    ],
                [
                    'td',
                    {'class':'text-center'},
                    lambda i: str(i.text).startswith('\n')
                    ],
                [0,5,0]
            ],
        'torrentglaxy': # torrentglaxy
            [
                'https://torrentgalaxy.to',
                f"/torrents.php?search={args.name}",
                [
                    {'title':True,'class':'txlight'},
                    lambda i: re.match(r'\d',str(i.text))
                    ],
                [
                    'div',
                    {'class':'tgxtablecell collapsehide rounded txlight'},
                    lambda i: bool(str(i.text).startswith('\n') and str(i.text) != '-' and str(i.text) != '')
                    ],
                [4,5,4]
            ],
#        'r': # rarbg
#            [
#                'https://rarbg.unblockninja.com',
#                f"/search/?search={args.name}",
#                [
#                    {'href':True,'title':True},
#                    lambda i: str(i.text).startswith('\n')
#                    ],
#                [
#                    'td',
#                    {'class':'lista'},
#                    lambda i : str(i.text).startswith('\n')
#                    ],
#                [0,6,0]
#            ],
        'eztv': # eztv
            [
                'https://eztv.re',
                f"/search/{args.name}",
                [
                    {'href':True,'title':True,'class':'epinfo'},
                    lambda i: False
                    ],
                [
                    'td',
                    {'align':'center','title':False},
                    lambda i: str(i.text).startswith('\n')
                    ],
                [1,3,1]
            ],
        '1337x': # 1337x
            [
                'https://1337x.wtf',
                f"/search/{args.name}/1/",
                [
                    {'href':True},
                    lambda i: not str(i.get('href')).startswith('/torrent')
                    ],
                [
                    'td',
                    {'class':True},
                    lambda i: not bool(str(i.get('class')[0]) != 'coll-1')
                    ],
                [0,5,0]
            ],
        }

def main():

    # instance of website object
    website = WebSite(provider[args.website][0],provider[args.website][1])
    # scrape provider website with search name
    website.scrape(website.url)
    # filter names only
    website.names =  [i for i in website.soup.find_all('a',provider[args.website][2][0]) if not provider[args.website][2][1](i)]
    # filter infoes like size seeds ...
    website.info = [i.text for i in website.soup.find_all(provider[args.website][3][0],provider[args.website][3][1]) if not provider[args.website][3][2](i)]
    # custom print
    website.prin_t(provider[args.website][-1])
    # take choice number
    website.s_url += website.names[int(input('enter the number:'))].get('href')
    # default behavior is printing magnet link
    website.magnet()
    print(website.magnet[0])
    sys.exit(0)

if __name__ == '__main__':
    main()
