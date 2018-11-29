import csv
from collections import Counter
b = []

def jadisatu(namadatacsv):
    global b
    with open(namadatacsv, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    for a in range(0,len(your_list)-1):
        b = b+your_list[a]+your_list[a+1]
    
    
jadisatu('databersih1.csv')
jadisatu('databersih2.csv')
jadisatu('databersih3.csv')
jadisatu('databersih4.csv')
jadisatu('databersih5.csv')
c = ' '.join(b)
d = c.split(' ')
counts = Counter(d)
#print(counts)
file = open('datapos.txt','w')
file.write(str(c))
file.close()

