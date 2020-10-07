from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/sms",methods=['POST'])
def sms_reply():
    """ respond to incoming calls """
    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message("you said: {}".format(msg))

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)