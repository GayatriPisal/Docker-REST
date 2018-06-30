import json
from flask import Flask,jsonify, render_template, request

app = Flask(__name__)
jsonData = json.loads(open('./playList.json').read())
data=jsonData["ShakespearePlays"]

@app.route('/')
def play_main():
    return render_template("index.html")

@app.route('/getplays/')
def play_all():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/getplays/<string:Year>/')
def play(Year=''):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
