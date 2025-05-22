from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from cowsay_generator import generate_cowsay

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tajnehaslo'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    name = data.get('name')
    color = data.get('color')
    text = data.get('text')
    cow = generate_cowsay(name, text, color)
    send(cow, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
