from flask import Flask, request

from message import Announcement, HelpRequest

app = Flask(__name__)

messages = []


@app.post('/announcement')
def announcement():
    message = Announcement(request.json['message'])
    messages.append(message)
    return {'success': True}


@app.post('/help-request')
def help_request():
    message = HelpRequest(request.json['message'], request.json['room'])
    messages.append(message)
    return {'success': True}


@app.get('/messages')
def get_messages():
    return {'messages': [str(message) for message in messages]}


if __name__ == '__main__':
    app.run()
