import pprint
import json
import gzip

__paths = ['qa_Appliances.json.gz',
    'qa_Automotive.json.gz',
    'qa_Baby.json.gz',
    'qa_Beauty.json.gz']

#read json file
def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield(eval(l))






if __name__=="__main__":
    data = parse(__paths[0])
    rs1 = {}
    qs = {}
    la = {}
    j = 1

    for i in data:
        
        rs1[j] = i['answer']
        qs[j] = i['question']
        la[j] = 'en'
        j+=1
        if j >= 50:
            break

    print(rs1)
    print(qs)

