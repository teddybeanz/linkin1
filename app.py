from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os
import webbrowser
import sys
import logging


from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processingRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
	
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processingRequest(req):
    if req.get("result").get("action") != "linking1":
        return{}
    webbrowser.open('http://google.com')
    
    new = 2
    tabURL = "http://google.com/?#q="
    webbrowser.open(tabURL, new=new)
	
 #   result = {'id': '609c2848-8bdc-40b8-9e7e-2baeaacda10f', 'timestamp': '2017-11-01T03:03:21.892Z', 'lang': 'en', 'result': {'source': 'agent', 'resolvedQuery': "i'd like to book a flight from singapore to tokyo this friday", 'action': '', 'actionIncomplete': False, 'parameters': {'date': '2017-11-03', 'destinationFrom': 'Singapore', 'destinationTo': 'Tokyo'}, 'contexts': [], 'metadata': {'intentId': '7dd793a3-e16f-45f0-867c-2e29be14d10d', 'webhookUsed': 'false', 'webhookForSlotFillingUsed': 'false', 'intentName': 'book.flight'}, 'fulfillment': {'speech': 'Hold on...Looking for flights available from Singapore to Tokyo on 2017-11-03', 'messages': [{'type': 0, 'speech': 'Give me a moment while I look for the flights available from Singapore to Tokyo on 2017-11-03'}]}, 'score': 0.9900000095367432}, 'status': {'code': 200, 'errorType': 'success'}, 'sessionId': 'aa2c9d04-9ba6-4f98-a8f0-a444547dce93'}
    result_data = json.dumps(req)
    data = json.loads(result_data)
    res=makeWebhookResult(data)
    return res
	


def makeWebhookResult(data):

   thedate = data['result']['parameters']['date']
#    one = data.get('results')
#	 if one is None:
#		return{}
	
#    two = one.get('parameters')
#	 if two is None:
#		return{}
#    third = two.get('date')
#	 if third is None:
#		return{}
	
    new = 2
    tabURL = "http://google.com/?#q="
    webbrowser.open(tabURL ,new=new)
 #   thedate = req.get("result").get("parameters").get("date")
 #   thedestinationFrom = req.get("result").get("parameters").get("destinationFrom")
 #   thedestinationTo = req.get("result").get("parameters").get("destinationTo")

    speech = "Hey no problem okay I'll look for flights on " + thedate 

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": data,
        #"contextOut": [],
        "source": "linking1"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
