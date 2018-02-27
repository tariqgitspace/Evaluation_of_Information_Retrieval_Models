import re
import json

without_hashtag = []

url_regex = r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b'
pattern = re.compile(url_regex)

with open('train.json',encoding="utf-8") as f:
        tweet = json.load(f)

        for value in tweet:
                if len(value["text_de"]) != 0: 
                        value["text_de"] = pattern.sub('', value["text_de"])
                            
                elif len(value["text_ru"]) != 0:
                        value["text_ru"] = pattern.sub('', value["text_ru"]) 

                elif len(value["text_en"]) != 0:
                        value["text_en"] = pattern.sub('', value["text_en"]) 

                without_hashtag.append(value)

outputFile = open('new_train.json','w')
outputFile.write(json.dumps(without_hashtag,ensure_ascii=False))
