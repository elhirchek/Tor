# Tor
A minimalist cli for surf/stream torrent or get magnet link

___

![preview](Preview.gif)

## Supported Websites

* 1337x 
* Nyaa
* TorrentGalaxy
* Eztv
* ~~Rarbg~~
* ~~subscence~~ (use [submpv](https://github.com/yassin-l/submpv))

## 1. Installation 

#### Dependencies

- Python 3
- Pip
- Nuitka for compilation (optional)
- ~~Mpv/peerflix for stream (optional)~~

> Note: For windows source code installation you will need MinGw64.
### Linux or Windows
```bash
git clone https://github.com/yassin-l/tor && cd tor

pip install -r requirements.txt 

# To add tor to your path env
ln ./tor /usr/bin/tor
```
> Note: change `default_webiste = "1337x"` to you're most used website instead of typing it everytime
##### For Compiling (it's optional)
> python -m nuitka --onefile -o tor tor.py 
## 2. Usage
```bash
usage: tor [-h] [-w website] name

positional arguments:
  name        Movie/Anime/Tvshow

options:
  -h, --help  show this help message and exit
  -w website  available website to query from: ['nyaa', 'torrentglaxy', 'eztv',
              '1337x']
```
### Example
```bash
tor -w1337x "breaking.bad" 
0 ==> Breaking Bad Season 2 Complete (1080p)
['TV/HD', '2021-09-20 11:03:34', '9.2 GB', '0\n', '0', 'eluway']
1 ==> Breaking Bad Season 3 Complete (1080p)
['TV/HD', '2021-09-20 11:03:34', '7.5 GB', '1\n', '0', 'eluway']
2 ==> Breaking Bad Season 4 Complete (1080)
['TV/HD', '2021-09-20 11:03:34', '6.8 GB', '0\n', '0', 'eluway']
3 ==> Breaking Bad S01 2008 720p 10bit BluRay English AAC 5.1 x265 - mkvAnime [Telly]
['TV/HEVC/x265', '2021-07-01 11:25:44', '2.4 GB', '17\n', '7', 'movieslover']
4 ==> Breaking Bad S04 2011 720p 10bit BluRay English AAC 5.1 x265 - mkvAnime [Telly]
['TV/HEVC/x265', '2021-07-01 11:01:03', '4.3 GB', '10\n', '6', 'movieslover']
5 ==> Breaking Bad S05 2012 720p 10bit BluRay English AAC 5.1 x265 - mkvAnime [Telly]
['TV/HEVC/x265', '2021-07-01 11:01:03', '5.4 GB', '9\n', '7', 'movieslover']
6 ==> Breaking Bad S02 2009 720p 10bit BluRay English AAC 5.1 x265 - mkvAnime [Telly]
['TV/HEVC/x265', '2021-07-01 11:01:02', '4.3 GB', '14\n', '9', 'movieslover']
7 ==> Breaking Bad S03 2010 720p 10bit BluRay English AAC 5.1 x265 - mkvAnime [Telly]
['TV/HEVC/x265', '2021-07-01 11:01:02', '4.3 GB', '12\n', '6', 'movieslover']
8 ==> Breaking Bad S01-05e01-62 DVD9 - Ita Eng Ger Fra Spa Cec Pol - MultiSub 21 DVD - SERIE COMPLETA
['TV/DVD', '2021-03-15 11:04:22', '148.5 GB', '0\n', '2', 'Plusam']
9 ==> Breaking Bad (2008) Season 1-5 S01-S05 (1080p BluRay x265 HEVC 10bit AAC 5.1 Silence) [QxR]
['TV/HEVC/x265', '2021-02-25 11:05:49', '140.1 GB', '58\n', '208', 'QxR']
10 ==> El.Camino.A.Breaking.Bad.Movie.2019.1080p.WEBRip.x264-WOW
['Movies/HD', '2020-11-14 11:03:56', '1.8 GB', '7\n', '1', 'jalim']
```

### Task List

- [X] ~~add subscene~~
- [ ] add The Pirate Bay
- [ ] add check stage for dependencies
