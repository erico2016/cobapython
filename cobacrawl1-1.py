import scrapy
import re
import csv
import nltk

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = re.sub(r'[^\w]', ' ', string)
    string = re.sub('\s+', ' ', string)

    return string.strip().lower() #.split()


class BrickSetSpider(scrapy.Spider):
    name = "www.smstauhiid.com"
    start_urls = ['http://www.smstauhiid.com/category/berita/','http://www.smstauhiid.com/category/alquran/','http://www.smstauhiid.com/category/ulama/','http://www.smstauhiid.com/category/kajian/','http://www.smstauhiid.com/category/khutbah-jumat/','http://www.smstauhiid.com/category/konsultasi/','http://www.smstauhiid.com/category/kumpulan-doa/']
    
    def parse(self, response):
        for i in range(1,10):
            SET_SELECTOR = 'article.item-list.item_'+str(i)                       
            brickset = response.css(SET_SELECTOR)
            NAME_SELECTOR = 'h2.post-title a ::text'
            DESKRIPSI_SELECTOR = 'div.entry p ::text' 
            if brickset.css(NAME_SELECTOR).extract_first() == None:
                break
            a = brickset.css(NAME_SELECTOR).extract_first()            
            b = brickset.css(DESKRIPSI_SELECTOR).extract_first()
            clean_a = clean_str(a)
            clean_b = clean_str(b)
            totalsemua = clean_a + clean_b
            yield {
                'kata' : totalsemua
            }
        NEXT_PAGE_SELECTOR = '#tie-next-page a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

