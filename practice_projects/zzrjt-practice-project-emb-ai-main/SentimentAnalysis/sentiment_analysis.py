''' This module contains functions to perform sentiment analysis
    using an external API and OpenAI's GPT model.
'''
import json
import requests
from openai import OpenAI

def sentiment_analyzer(text_to_analyse):
    ''' This function takes a text input and sends it to an external
        sentiment analysis API. It returns the sentiment label and
        confidence score.
    '''
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network' \
            '/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=10)

    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return { "label": label, "score": score }

def openai_sentiment_analyzer(text_to_analyse):
    ''' This function takes a text input and uses OpenAI's GPT model
        to perform sentiment analysis. It returns the sentiment label
        and confidence score.
    '''
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": '''
                You are a sentiment analysis model.
             You will classify the sentiment of the given text as
                label: SENT_POSITIVE, SENT_NEGATIVE, or SENT_NEUTRAL.
             Score should be a float between 0 and 1 indicating confidence.
             Response with a json only with properties { label, score }.'''},
            {"role": "user", "content":
                f"Classify the sentiment of the following text: '{text_to_analyse}'"}
        ],
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    sentiment = response.choices[0].message.content.strip()
    print( "OpenAI Response: ", response )
    print( "Sentiment Analysis Response: ", sentiment )

    # catch errors in json response
    try:
        formatted_response = json.loads(sentiment)
    except json.JSONDecodeError:
        return { "label": "SENT_NEUTRAL", "score": 0.0 }

    return { "label": formatted_response['label'], "score": formatted_response['score'] }
