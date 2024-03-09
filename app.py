from flask import Flask, render_template, jsonify, request
from YTSentiment import *

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/analyze', methods=['POST', 'GET'], )
def analyze():
    analyze_data_set()
    body = request.data.decode('utf-8')

    if body == "": 
        sentiment_result = "neutral"
        analysis_result = "(The title was empty)"
        return jsonify({
            'sentiment': sentiment_result,
            'views': analysis_result
        })
    
    # if not empty then do the analysis and return 
    sentiment_result = sent_string(sent(body))   
    analysis_result = analyze_input(body)
    return jsonify({
        'sentiment': sentiment_result,
        'views': analysis_result
    })

    # """
    # # result = 
    # Sentiment of title: {Positive}
    # Projected number of views: {633,000} views


    # number_str = "633000"
    # formatted_number = f"{int(number_str):,}"
    # print(formatted_number)




    # # 
    # """