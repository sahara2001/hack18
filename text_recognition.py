#voice recognition module that translate voice to text
import urllib
import requests
from pprint import pprint
from process import parse,__paths
from difflib import SequenceMatcher


#header for the request
headers = {
    'Ocp-Apim-Subscription-Key': 'df4a2931779949c0a141a4815d19fca8',
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

processed_database = 'output'

# The function get document meaning specified by option and return it
# param: documents: dictionary that contain request file.
#        option: string specifying job to do
def get_option(documents, option):

    text_analytics_base_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/"
    language_api_url = text_analytics_base_url + option

    response = requests.post(language_api_url, headers=headers, json=documents)
    languages = response.json()
    pprint(languages)
    return languages

def process_set(questions, languages,option='keyPhrases'):
    set1 = {}
    set1['documents'] = []
    doc1 = []

    for i in range(0,len(questions)):
        diction1 = {'id':str(i),'language': languages[i],'text':questions[i]}
        doc1.append(diction1)

    set1['documents'] = doc1
    result = get_option(set1,option)
    return result

#ask is either zero or not to denote if the user is asking question
def dataset_process(index, ask=0):
    data = parse(__paths[0])
    rs1 = {}
    qs = {}
    la = {}
    j = 0

    for i in data:
        
        rs1[j] = i['answer']
        qs[j] = i['question']
        la[j] = 'en'
        j+=1
        if j >= 500:
            break

        

    Answers = process_set(rs1,la)
    Questions = process_set(qs,la)
    #store data for backup
    with open('Answers','w') as r:
        for l in Answers['documents']:
            r.write(str(l)+'\n')

    with open('Questions', 'w') as w:
        for l in Questions['documents']:
            w.write(str(l)+'\n')

    




#read json file 
def parse_processed_question():
    with open('Questions', 'r') as q:
        for l in q:
            yield(eval(l))

#read json file
def parse_processed_answer():
    with open('Answers', 'r') as q:
        for l in q:
            yield(eval(l))

#the match uses key phrases to match similar question-answer pair, question here denote whether the query is a question 
def keyword_match(index,question=True):
    matches = []
    answers = parse_processed_answer()
    questions = parse_processed_question()
    if question:
        tmp = next(questions)
        seq1 = ' '.join(next(questions)['keyPhrases'])
        index = 1
        for i in parse_processed_answer():
            seq2 = ' '.join(i['keyPhrases'])
            
            dist = SequenceMatcher(None,seq1,seq2).ratio()*len(seq1)*len(seq2)
            if dist >= 15:
                print(seq1)
                print(seq2)
                print(dist)
                matches.append(index)
                
            index += 1
        
    if not question:
        seq1 = ' '.join(next(answers)['keyPhrases'])
        index = 1
        for i in parse_processed_question():
            seq2 = ' '.join(i['keyPhrases'])
            
            dist = SequenceMatcher(None,seq1,seq2).ratio()
            if dist >= 0.4:
                print(seq1)
                print(seq2)
                print(dist)
                matches.append(index)
                
            index += 1
    return matches

#this match uses whole sentences to match and uses Levenshtein module




if __name__=='__main__':
    """
    documents1 = {'documents' : [
        {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
        {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
        {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
        {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
    ]}
    documents2 = {'documents' : [
        {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
        {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
        {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
        {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
    ]}
    documents3 = {'documents' : [
        {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
        {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
        {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
        {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
    ]}
    option1 = 'languages'
    option2 = 'sentiment'
    option3 = 'keyPhrases'
    dataset_process(1)
    """
    
    keyword_match(0,1)
    s1 = 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'
    s2 = 'I had a terrible time at the hotel. The staff was rude and the food was awful.'
    print(SequenceMatcher(None, s1, s2).ratio())
