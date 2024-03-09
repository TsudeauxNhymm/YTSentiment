from flask import Flask, render_template, jsonify, request
from YTSentiment import *

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')


# TODO:
"""
Upon loading the page it calls the analyze_csv fn. 
"""


@app.route('/analyze_fetch', methods=['POST', 'GET'], )
def analyze_fetch():
    analyze_data_set()
    body = request.data.decode('utf-8')
    analysis_result = "Title is empty" if body == "" else analyze_input(body)


    """
    # result = "Sentiment of title: {Positive}"
    # 
    """





    analysis_result = analyze_input(request.data.decode('utf-8'))
    return jsonify({
        'result': analysis_result
    })
