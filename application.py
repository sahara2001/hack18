from flask import Flask, request
from voice_cognition import get_option
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chat")
def chat():
    return "Hello!"

@app.route('/match', methods=['GET','POST'])
def match():
    documents3 = {'documents' : [
        {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
        {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
        {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
        {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
    ]}
    option = 'keyPhrases'
    result = get_option(documents3, option)

    error = None
    if request.method == 'POST':
        if request.form['username']!= None and request.form['doc']!=None:
            return "good"
        else:
            error = 'Invalid username/password'
    else:
        return "please request data"


    return result
