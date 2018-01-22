from lxml import etree
from io import StringIO
import urllib

url = 'https://en.wikipedia.org/wiki/2017–18_Anaheim_Ducks_season#Regular_season'
root = etree.parse(urllib.urlopen(url))

for obs in root.xpath('/ff:DataSet/ff:Series/ff:Obs'):
    price = obs.xpath('./base:OBS_VALUE').text
    print(price)
