# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""

import json
# if you are using python 3, you should 
import urllib.request 
#import urllib2
import os

# change the url according to your own koding username and query
##inurl = 'http://localhost:8983/solr/corename/select?q=*%3A*&fl=id%2Cscore&wt=json&indent=true&rows=1000'
#inurl =   'http://54.191.113.44:8983/solr/BM25/select?q=*%3A*&fl=id%2Cscore&wt=json&indent=true&rows=1000'



# change query id and IRModel name accordingly
#qid = ''
model='DFR'
count = 1
if os.path.isfile(model+'.txt'):
    print("removed")
    os.remove(model+'.txt')

with open('queries.txt', encoding="utf-8") as f:
    for line in f:
        query=line[4:len(line)]
        query = line.strip('\n').replace(':', '')
        query = urllib.parse.quote(query)

        ##weights = 'tweet_hashtags^2.04%20text_en^2.25%20text_de^2.0%20text_ru^2.0'
        ##weights = 'tweet_hashtags^2.04%20text_en^'+str(weight_en)+'%20text_de^'+str(weight_de)+'%20text_ru^'+str(weight_ru)
        ##pf = 'tweet_hashtags^4.0%20text_en^'+str(2*weight_en)+'%20text_de^'+str(2*weight_de)+'%20text_ru^'+str(2*weight_ru)
        ##print(weights)
        ##inurl = 'http://54.191.113.44:8983/solr/'+ model +'/select?defType=dismax&fl=id,score&indent=on&q=' + query + '&qf='+ weights +'&pf='+ pf + '&rows=20&wt=json'

        inurl = 'http://54.191.113.44:8983/solr/'+ model +'/select?fl=id,score&indent=on&q=' + query + '&rows=20&wt=json'    
        ##inurl = 'http://54.191.113.44:8983/solr/DFR/select?fl=id,score&indent=on&q=' + query + '&rows=20&wt=json'
        outf = open(model+'.txt', 'a+')
        data = urllib.request.urlopen(inurl).read()
        docs = json.loads(data.decode('utf-8'))['response']['docs']
        rank = 0
        for doc in docs:
            outf.write(str(format(count, "03d")) + ' ' + 'Q' + str(count-1) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + model + '\n')
            rank += 1
        outf.close()
        count += 1
        outf.close()
