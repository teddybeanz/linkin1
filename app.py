from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os
import webbrowser


from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


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
<<<<<<< HEAD
    
    new = 2
    tabURL = "http://google.com/?#q="
    webbrowser.open(tabURL + row,new=new)
=======
>>>>>>> 04d6b61e3b46c9366080196eb6eb84c1d4c056a9

    data = json.loads(result)
    res=makeWebhookResult(data)
    return res
	


def makeWebhookResult(data):

    webbrowser.open('http://google.com')
    thedate = data['result']['parameters']['date']

<<<<<<< HEAD
    new = 2
    tabURL = "http://google.com/?#q="
    webbrowser.open(tabURL + row,new=new)
=======
>>>>>>> 04d6b61e3b46c9366080196eb6eb84c1d4c056a9
	
    speech = "Hey no problem okay I'll look for flights on" + thedate 

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "data": data,
        "contextOut": [],
        "source": "linking1"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
