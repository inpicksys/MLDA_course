import requests
import bs4
from multiprocessing import Pool
import codecs
from functools import reduce

def parse_page(url):
    text = requests.get(url).text
    parser = bs4.BeautifulSoup(text, 'lxml')
    x = parser.findAll('div', attrs={'class':'text'})
    return [res.text for res in x]

#p = Pool(10)
url_list = ['http://zadolba.li/201604' + '0' * int(n < 10) + str(n) for n in range(1, 3)]
    
if __name__ == '__main__':
    with Pool(10) as p:
        map_results = p.map(parse_page, url_list)
    reduce_results = reduce(lambda x,y: x + y, map_results)
    with codecs.open('parsing_results.txt', 'w', 'utf-8') as output_file:
        print(u'\n'.join(reduce_results), file=output_file)