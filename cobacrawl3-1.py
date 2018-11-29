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
    name = "http://nusantara.rmol.co/"
    start_urls = ['http://nusantara.rmol.co/']
    
    def parse(self, response):
        SET_SELECTOR = 'div.post-item.post-sticky'    
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'div.title h2 a ::text'
            DESKRIPSI_SELECTOR = 'div.caption-ucan p a::text' 
            #if brickset.css(NAME_SELECTOR).extract_first() == None:
            #    break
            a = brickset.css(NAME_SELECTOR).extract_first()            
            b = brickset.css(DESKRIPSI_SELECTOR).extract_first()
            clean_a = clean_str(a)
            clean_b = clean_str(b)
            totalsemua = clean_a + clean_b
            yield {
                'kata' : totalsemua                
            }
        
        NEXT_PAGE_SELECTOR = 'div.col-md-12.text-center.mb-20 a.next.page-numbers::attr(href)'        
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
        
