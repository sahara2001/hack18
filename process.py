import pprint
import json
import gzip


#read json file
def parse():

    j=0
    data={}
    path = ['qa_Appliances.json.gz',
    'qa_Automotive.json.gz',
    'qa_Baby.json.gz',
    'qa_Beauty.json.gz']

    g = gzip.open(path[0], 'r')
    for l in g:
        data[j]=eval(l)
        j+=1
    return data




if __name__=="__main__":
    pprint.pprint(parse()[1]['answer'])
