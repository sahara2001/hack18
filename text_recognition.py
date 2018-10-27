#voice recognition module that translate voice to text
import urllib
import requests
from pprint import pprint

#header for the request
headers = {
    'Ocp-Apim-Subscription-Key': 'df4a2931779949c0a141a4815d19fca8',
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

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







if __name__=='__main__':
    
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
    get_option(documents1, option1)
    get_option(documents2, option2)
    get_option(documents3, option3)
